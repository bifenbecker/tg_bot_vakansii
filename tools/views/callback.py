from __future__ import annotations
from typing import TYPE_CHECKING, Union, Optional
from telebot import types
from tools.views.handlers import CallbackHandler

if TYPE_CHECKING:
    from bot import Bot


class CallbackView(CallbackHandler):
    TEXT_FOR_KEYBOARD = ""
    INLINE_KEYBOARD = None

    def entry_render(self, data: Optional[dict] = None):
        self.bot.send_reply_message(self.TEXT_FOR_KEYBOARD, reply_markup=self.INLINE_KEYBOARD)

