from time import sleep
from typing import Optional, Union, Type
from telebot import types, TeleBot
from importlib import import_module
from glob import glob
from tools.views import View
from tools.components import Menu, InlineKeyboard, ViewManager, HashMapUsersManager
from apps.test.views import View1

import logging

logging.basicConfig()
logger = logging.getLogger(__name__)


class Bot:

    def __init__(self, token: str, *args, **kwargs):
        self._bot: TeleBot = TeleBot(token=token, *args, **kwargs)
        views_modules = [package.replace("/", ".") for package in glob("apps/**/views")]
        self.users_manager = HashMapUsersManager(bot=self, view_manager_type=ViewManager.QueueViewManager)

        self._bot.set_my_commands([
            types.BotCommand("/start", "start")
        ])

        self._bot.register_message_handler(self.on_start_command, commands=["start"])

        for views_module in views_modules:
            module = import_module(views_module)
            for item_name in module.__all__:
                _View: View = getattr(module, item_name)
                instance_view = _View.create(self)
                instance_view.register_view()

    def on_start_command(self, message: types.Message):
        self.users_manager.add_user(user=message.from_user)
        self.switch_view(user=message.from_user, next_view=View1)

    def delete_message(self, chat_id: Union[str, int], message_id: Union[str, int],
                       timeout: Optional[int] = None) -> bool:
        return self._bot.delete_message(chat_id=chat_id, message_id=message_id, timeout=timeout)

    def remove_menu(self, menu: Menu):
        # TODO: Fix. Delete reply menu without deleting and sending message. Edit message throw 400 error
        pass

    def remove_menu_with_message(self, chat_id: Union[str, int], text: str, menu: Menu) -> types.Message:
        return self._bot.send_message(chat_id=chat_id, text=text, reply_markup=menu.remove())

    def send_message_with_menu(self, chat_id: Union[str, int], text: str, menu: Menu) -> types.Message:
        return self._bot.send_message(chat_id=chat_id, text=text, reply_markup=menu.keyboard)

    def send_message_with_inline_keyboard(self, chat_id: Union[str, int], text: str,
                                          inline_keyboard: InlineKeyboard) -> types.Message:
        return self._bot.send_message(chat_id=chat_id, text=text, reply_markup=inline_keyboard.keyboard)

    def run(self):
        self._bot.polling(none_stop=True, skip_pending=True)

    def switch_view(self, user: types.User, next_view: Type[View], exit_view: bool = True,
                    data_to_next_view: Optional[dict] = None,
                    entry_view: bool = True):
        self.users_manager.switch_view_for_user(user=user, next_view=next_view, data=data_to_next_view,
                                                exit_view=exit_view, entry_view=entry_view)

    def back_view(self, user: types.User, data: Optional[dict] = None, exit_view: bool = True, entry_view: bool = True):
        self.users_manager.back_view_for_user(user=user, data=data, exit_view=exit_view, entry_view=entry_view)

    def current_view(self, message: types.Message) -> Optional[Type[View]]:
        return self.users_manager.current_view_for_user(user=message.from_user)

    @property
    def telegram_api(self):
        return self._bot
