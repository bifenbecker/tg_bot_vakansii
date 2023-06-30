from __future__ import annotations
from typing import TYPE_CHECKING, Union, Optional
from telebot import types
from tools.views import CallbackView, View, SimpleTextView, MenuView
from tools.components import Menu, Button
from tools.views.handlers import MessageHandler, CallbackHandler, MultiHandlerView

if TYPE_CHECKING:
    from bot import Bot


class View1(CallbackView):
    TEXT_WITH_INLINE_KEYBOARD = "Test"
    INLINE_KEYBOARD = types.InlineKeyboardMarkup().add(
        types.InlineKeyboardButton("Test", callback_data="data")
    )

    def callback_handler(self, callback: types.CallbackQuery):
        print(callback.data)
