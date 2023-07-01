from __future__ import annotations
from typing import TYPE_CHECKING, Union, Optional, List
from telebot import types
from tools.views import CallbackView, View, SimpleTextView, MenuView, PaginatedCallbackView
from tools.components import Menu, Button, InlineKeyboard, InlineButton
from tools.views.handlers import MessageHandler, CallbackHandler, MultiHandlerView
from .View2 import View2

if TYPE_CHECKING:
    from bot import Bot


class View1(MenuView, MessageHandler):

    def configure_menu(self, user: types.User) -> Menu:
        menu = Menu(
            Button("Test", to_view=View2)
        ).options(
            user=user,
            bot=self.bot,
            resize_keyboard=True,
            one_time_keyboard=True
        )
        return menu

    def text_for_menu(self, user: types.User) -> str:
        return "Test"

    def message_handler(self, message: types.Message):
        print(message)
