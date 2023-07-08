from __future__ import annotations
from typing import TYPE_CHECKING, Union
from telebot import types

if TYPE_CHECKING:
    from bot import Bot


class AnsweredHandleObject:

    def __init__(self, handle_object: Union[types.Message, types.CallbackQuery], bot: Bot):
        self._source = handle_object
        self._bot = bot

    @property
    def chat(self) -> types.Chat:
        return self._source.chat

    @property
    def chat_id(self) -> int:
        return self.chat.id

    @property
    def user(self) -> types.User:
        return self._source.from_user


