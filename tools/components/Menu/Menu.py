from typing import List, Optional, Union
from telebot import types
from .Button import Button


class Menu:
    buttons: List[Button]
    keyboard: types.ReplyKeyboardMarkup

    def __init__(self, *buttons: Button):
        self.buttons = [*buttons]
        self.keyboard = types.ReplyKeyboardMarkup().add(
            *[types.KeyboardButton(text=button.text) for button in self.buttons]
        )

    def options(self, resize_keyboard: Optional[bool] = None, one_time_keyboard: Optional[bool] = None,
                selective: Optional[bool] = None, row_width: int = 3, input_field_placeholder: Optional[str] = None,
                is_persistent: Optional[bool] = None):
        self.keyboard = types.ReplyKeyboardMarkup(resize_keyboard=resize_keyboard, one_time_keyboard=one_time_keyboard,
                                                  selective=selective, row_width=row_width,
                                                  input_field_placeholder=input_field_placeholder,
                                                  is_persistent=is_persistent).add(
            *[types.KeyboardButton(text=button.text) for button in self.buttons]
        )

    def remove(self) -> types.ReplyKeyboardRemove:
        return types.ReplyKeyboardRemove()
