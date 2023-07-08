from __future__ import annotations
from typing import TYPE_CHECKING
from telebot import types

if TYPE_CHECKING:
    from bot import Bot


class AnsweredMessage:

    def __init__(self, source_message: types.Message, bot: Bot):
        self._source_message = source_message
        self.bot = bot

    def answer(self, text: str) -> types.Message:
        return self.bot.telegram_api.send_message(chat_id=self._source_message.chat.id, text=text)

    @property
    def source(self) -> types.Message:
        return self._source_message
