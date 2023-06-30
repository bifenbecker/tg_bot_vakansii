from typing import Optional, Union, Type
from time import time
from telebot import types, TeleBot
from importlib import import_module
from glob import glob
from tools.views import View
from tools.components import Menu
from apps.test.views import View1


class Bot:
    _bot: TeleBot
    _user: Optional[types.User] = None
    __current_view: Optional[Type[View]] = None

    def __init__(self, token: str, *args, **kwargs):
        self._bot = TeleBot(token=token, *args, **kwargs)
        views_modules = [package.replace("/", ".") for package in glob("apps/**/views")]
        self.__current_view = None

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
                # _View.as_view(self)

    def on_start_command(self, message: types.Message):
        self._user = message.from_user
        self.switch_view(next_view=View1)

    def send_reply_message(self, text: str, *args, **kwargs) -> types.Message:
        return self._bot.send_message(chat_id=self._user.id, text=text, *args, **kwargs)

    def delete_message(self, chat_id: Union[str, int], message_id: Union[str, int],
                       timeout: Optional[int] = None) -> bool:
        return self._bot.delete_message(chat_id=chat_id, message_id=message_id, timeout=timeout)

    def delete_reply_message(self, message_id: Union[str, int], timeout: Optional[int] = None) -> bool:
        return self.delete_message(chat_id=self._user.id, message_id=message_id, timeout=timeout)

    def remove_menu(self, menu: Menu):
        # TODO: Fix. Delete reply menu without deleting and sending message. Edit message throw 400 error
        msg_to_delete = self.remove_reply_menu_with_message(".", menu=menu)
        self.delete_reply_message(message_id=msg_to_delete.message_id)

    def remove_menu_with_message(self, chat_id: Union[str, int], text: str, menu: Menu) -> types.Message:
        return self._bot.send_message(chat_id=chat_id, text=text, reply_markup=menu.remove())

    def remove_reply_menu_with_message(self, text: str, menu: Menu) -> types.Message:
        return self.remove_menu_with_message(chat_id=self._user.id, text=text, menu=menu)

    def send_reply_message_with_menu(self, text: str, menu: Menu) -> types.Message:
        return self.send_message_with_menu(chat_id=self._user.id, text=text, menu=menu)

    def send_message_with_menu(self, chat_id: Union[str, int], text: str, menu: Menu) -> types.Message:
        return self._bot.send_message(chat_id=chat_id, text=text, reply_markup=menu.keyboard)

    def run(self):
        self._bot.polling(none_stop=True)

    def switch_view(self, next_view: Type[View], exit_prev: bool = True, data_to_next_view: Optional[dict] = None):
        prev_view = None
        if self.__current_view:
            instance = self.__current_view.create(self)
            if exit_prev:
                instance.exit()
            prev_view = instance
        self.__current_view = next_view
        instance = next_view.create(self)
        instance.prev_view = prev_view
        instance.entry(data=data_to_next_view)

    @property
    def current_view(self) -> Optional[View]:
        return self.__current_view

    @property
    def user(self) -> Optional[types.User]:
        return self._user

    @user.setter
    def user(self, new_user: types.User):
        self._user = new_user

    @property
    def telegram_api(self):
        return self._bot
