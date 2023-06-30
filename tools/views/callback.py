from __future__ import annotations
from typing import TYPE_CHECKING, Union, Optional
from telebot import types
from tools.views.handlers import CallbackHandler
from tools.middlewares import MiddlewaresType

if TYPE_CHECKING:
    from bot import Bot


class CallbackView(CallbackHandler):
    TEXT_WITH_INLINE_KEYBOARD = ""
    INLINE_KEYBOARD = None

    MIDDLEWARES = {
        MiddlewaresType.AFTER_ENTRY: [
            "after_entry_render_inline_keyboard",
        ],
    }

    def after_entry_render_inline_keyboard(self, data):
        self.bot.send_reply_message(self.TEXT_WITH_INLINE_KEYBOARD, reply_markup=self.INLINE_KEYBOARD)


# Example
# class View1(CallbackView):
#     TEXT_WITH_INLINE_KEYBOARD = "Test"
#     INLINE_KEYBOARD = types.InlineKeyboardMarkup().add(
#         types.InlineKeyboardButton("Test", callback_data="data")
#     )
#
#     def callback_handler(self, callback: types.CallbackQuery):
#         print(callback.data)


