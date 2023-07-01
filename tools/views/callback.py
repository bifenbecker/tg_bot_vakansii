from __future__ import annotations
from typing import TYPE_CHECKING, Union, Optional
from telebot import types
from tools.views.handlers import CallbackHandler
from tools.middlewares import MiddlewaresType
from tools.components import InlineKeyboard

if TYPE_CHECKING:
    from bot import Bot


class CallbackView(CallbackHandler):
    TEXT_WITH_INLINE_KEYBOARD: Optional[str] = None
    INLINE_KEYBOARD: Optional[InlineKeyboard] = None

    MIDDLEWARES = {
        MiddlewaresType.BEFORE_ENTRY: [
            "configurate_inline_keyboard",
        ],
        MiddlewaresType.AFTER_ENTRY: [
            "after_entry_render_inline_keyboard",
        ],
    }

    def __init__(self, bot, *args, **kwargs):
        super().__init__(bot, args, kwargs)
        self.message: Optional[types.Message] = None

    def configurate_inline_keyboard(self, data):
        pass

    def after_entry_render_inline_keyboard(self, user, data):
        if not self.TEXT_WITH_INLINE_KEYBOARD or not self.INLINE_KEYBOARD:
            raise Exception("Define 'TEXT_WITH_INLINE_KEYBOARD' and 'INLINE_KEYBOARD'. They are required")
        self.message = self.bot.send_message_with_inline_keyboard(chat_id=user.id, text=self.TEXT_WITH_INLINE_KEYBOARD,
                                                                        inline_keyboard=self.INLINE_KEYBOARD)

# Example
# class View1(CallbackView):
#     TEXT_WITH_INLINE_KEYBOARD = "Test"
#     INLINE_KEYBOARD = types.InlineKeyboardMarkup().add(
#         types.InlineKeyboardButton("Test", callback_data="data")
#     )
#
#     def callback_handler(self, callback: types.CallbackQuery):
#         print(callback.data)
