from __future__ import annotations
from typing import Callable, TYPE_CHECKING
from telebot import types
from tools.components import AnsweredMessage


if TYPE_CHECKING:
    from bot import Bot


class HandlerMixin:

    def _get_message_handler(self, bot: Bot) -> Callable:
        def source_message_handler(message: types.Message):
            answered_message = self.source_message_handler(message=message, bot=bot)
            self.message_handler(message=answered_message)
        return source_message_handler

    def source_message_handler(self, message: types.Message, bot) -> AnsweredMessage:
        return AnsweredMessage(source_message=message, bot=bot)

    def message_handler(self, message: AnsweredMessage):
        pass

    def callback_handler(self, callback: types.CallbackQuery):
        pass

    def file_handler(self, message: types.Message):
        pass

    def document_handler(self, message: types.Message):
        pass

    def photo_handler(self, message: types.Message):
        pass

    def voice_handler(self, message: types.Message):
        pass

    def contact_handler(self, message: types.Message):
        pass
