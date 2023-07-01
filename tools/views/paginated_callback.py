from __future__ import annotations
from typing import TYPE_CHECKING, Union, Optional, List
from telebot import types
from tools.views import CallbackView
from tools.components import InlineKeyboard, InlineButton
from tools.middlewares import MiddlewaresType


class PaginatedCallbackView(CallbackView):
    NEXT_BUTTON_TEXT: str = "Next"
    PREVIOUS_BUTTON_TEXT: str = "Back"

    MIDDLEWARES = {
        MiddlewaresType.BEFORE_ENTRY: [
            "get_inline_keyboard_paginated_options",
        ],
        MiddlewaresType.AFTER_HANDLER: [
            "on_click_inline_button",
        ]
    }

    def get_inline_keyboard_paginated_options(self, data, option: Optional[str] = None) -> List[InlineButton]:
        pass

    def after_entry_render_inline_keyboard(self, data):
        self.INLINE_KEYBOARD = InlineKeyboard(
            InlineButton(text=self.PREVIOUS_BUTTON_TEXT, callback_data="prev",
                         on_click=self.on_click_prev_inline_button),
            *self.get_inline_keyboard_paginated_options(data=data),
            InlineButton(text=self.NEXT_BUTTON_TEXT, callback_data="next", on_click=self.on_click_next_inline_button)
        )
        super().after_entry_render_inline_keyboard(data=data)

    def on_click_prev_inline_button(self):
        self.bot.telegram_api.edit_message_reply_markup(chat_id=self.bot.user.id, message_id=self.message.message_id,
                                                        reply_markup=InlineKeyboard(
                                                            InlineButton(text=self.PREVIOUS_BUTTON_TEXT,
                                                                         callback_data="prev",
                                                                         on_click=self.on_click_prev_inline_button),
                                                            *self.get_inline_keyboard_paginated_options(data={},
                                                                                                        option="prev"),
                                                            InlineButton(text=self.NEXT_BUTTON_TEXT,
                                                                         callback_data="next",
                                                                         on_click=self.on_click_next_inline_button)
                                                        ).keyboard)

    def on_click_next_inline_button(self):
        self.bot.telegram_api.edit_message_reply_markup(chat_id=self.bot.user.id, message_id=self.message.message_id,
                                                        reply_markup=InlineKeyboard(
                                                            InlineButton(text=self.PREVIOUS_BUTTON_TEXT,
                                                                         callback_data="prev",
                                                                         on_click=self.on_click_prev_inline_button),
                                                            *self.get_inline_keyboard_paginated_options(data={},
                                                                                                        option="next"),
                                                            InlineButton(text=self.NEXT_BUTTON_TEXT,
                                                                         callback_data="next",
                                                                         on_click=self.on_click_next_inline_button)
                                                        ).keyboard)

    def on_click_inline_button(self, handle_obj: types.CallbackQuery):
        for button in self.INLINE_KEYBOARD.buttons:
            if button.callback_data == handle_obj.data:
                button.action(switch_view=self.bot.switch_view)
