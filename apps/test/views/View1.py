from __future__ import annotations
from typing import TYPE_CHECKING, Union, Optional
from telebot import types
from tools.views import CallbackView
from tools.components import Menu, Button
from tools.views.handlers import MessageHandler, CallbackHandler

if TYPE_CHECKING:
    from bot import Bot


class View1(CallbackView):
    TEXT_FOR_KEYBOARD = "TEST"
    INLINE_KEYBOARD = types.InlineKeyboardMarkup().add(
        types.InlineKeyboardButton("Btn1", callback_data="btn1")
    )

    def callback_handler(self, callback: types.CallbackQuery):
        print(callback)
