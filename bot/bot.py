from typing import Optional, Union, Type
from telebot import types, TeleBot
from importlib import import_module
from glob import glob
from tools.views import View


class Bot:
    _bot: TeleBot
    _user: Optional[types.User] = None
    __current_view: Optional[Type[View]] = None

    def __init__(self, token: str, *args, **kwargs):
        self._bot = TeleBot(token=token, *args, **kwargs)
        views_modules = [package.replace("/", ".") for package in glob("apps/**/views")]
        self.__current_view = None

        for views_module in views_modules:
            module = import_module(views_module)
            for item_name in module.__all__:
                _View: View = getattr(module, item_name)
                _View.as_view(self)

    def register_message_handler(self, handler, *args, **kwargs):
        self._bot.register_message_handler(handler, *args, **kwargs)

    def register_next_step_handler(self, message, callback, *args, **kwargs):
        self._bot.register_next_step_handler(message, callback, *args, **kwargs)

    def register_callback_handler(self, handler, *args, **kwargs):
        self._bot.register_callback_query_handler(handler, *args, **kwargs)

    def send_message(self, to: Union[str, int], message: str,
                     reply_markup: Optional[types.InlineKeyboardMarkup] = None):
        self._bot.send_message(chat_id=to, text=message, reply_markup=reply_markup)

    def run(self):
        self._bot.polling(none_stop=True)

    def switch_view(self, next_view: Type[View]):
        self.__current_view.exit()
        self.__current_view = next_view
        instance = next_view.create(self)
        instance.entry()

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
