from __future__ import annotations
from typing import List, Optional, TYPE_CHECKING
from telebot import types
from .Button import InlineButton

if TYPE_CHECKING:
    from bot import Bot


class InlineKeyboard:
    _bot: Optional[Bot]
    buttons: List[InlineButton]
    keyboard: types.InlineKeyboardMarkup

    def __init__(self, *buttons: InlineButton):
        self._bot = None
        self.buttons = [*buttons]
        self.keyboard = types.InlineKeyboardMarkup().add(
            *[types.InlineKeyboardButton(text=button.text, callback_data=button.callback_data) for button in
              self.buttons]
        )

    @property
    def bot(self) -> Bot:
        return self._bot

    @bot.setter
    def bot(self, new_bot: Bot):
        self._bot = new_bot

