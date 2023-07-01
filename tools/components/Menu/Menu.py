from __future__ import annotations
from typing import List, Optional, TYPE_CHECKING, Union
from telebot import types
from .Button import Button

if TYPE_CHECKING:
    from bot import Bot


class Menu:
    _bot: Optional[Bot]
    buttons: List[Button]
    keyboard: types.ReplyKeyboardMarkup

    def __init__(self, *buttons: Button):
        self._bot: Optional[Bot] = None
        self._user: Optional[types.User] = None
        self._handle_obj: Union[types.Message, types.CallbackQuery, None] = None
        self.buttons = [*buttons]
        self.keyboard = types.ReplyKeyboardMarkup().add(
            *[types.KeyboardButton(text=button.text) for button in self.buttons]
        )

    @property
    def bot(self) -> Bot:
        return self._bot

    @bot.setter
    def bot(self, new_bot: Bot):
        self._bot = new_bot

    @property
    def user(self) -> types.User:
        return self._user

    @user.setter
    def user(self, _obj: types.User):
        self._user = _obj

    def options(self, user: types.User, bot: Bot, handle_obj: Union[types.Message, types.CallbackQuery, None] = None,
                resize_keyboard: Optional[bool] = None, one_time_keyboard: Optional[bool] = None,
                selective: Optional[bool] = None, row_width: int = 3, input_field_placeholder: Optional[str] = None,
                is_persistent: Optional[bool] = None) -> Menu:
        self._user = user
        self._bot = bot
        self._handle_obj = handle_obj
        self.keyboard = types.ReplyKeyboardMarkup(resize_keyboard=resize_keyboard, one_time_keyboard=one_time_keyboard,
                                                  selective=selective, row_width=row_width,
                                                  input_field_placeholder=input_field_placeholder,
                                                  is_persistent=is_persistent).add(
            *[types.KeyboardButton(text=button.text) for button in self.buttons]
        )
        return self

    def action(self, button: Button, exit_prev: bool = True, entry_view: bool = True):
        return button.action(for_user=self._user, switch_view=self._bot.switch_view, exit_prev=exit_prev,
                             entry_view=entry_view)

    def remove(self) -> types.ReplyKeyboardRemove:
        return types.ReplyKeyboardRemove()
