from __future__ import annotations
from typing import TYPE_CHECKING
from telebot import types
from tools.views import View, MenuView
from tools.components import Menu, Button
from .View2 import View2

if TYPE_CHECKING:
    from bot import Bot


class View1(MenuView):
    # menu = Menu(
    #     Button("Btn 1"),
    #     Button("Btn 2")
    # )
    # .options(row_width=1, one_time_keyboard=True, resize_keyboard=True)

    def entry_text(self) -> str:
        return "View1 Entry"

    def reply_menu(self) -> Menu:
        return Menu(
            Button("Btn 1"),
            Button("Btn 2")
        )

    # def entry(self):
    # self.bot.send_reply_message_with_menu("View1 Entry", menu=self.menu)
    # self.bot.send_reply_message(message="View1 Entry",
    #                             reply_markup=types.ReplyKeyboardMarkup(row_width=1, one_time_keyboard=True,
    #                                                                    resize_keyboard=True, selective=True,
    #                                                                    is_persistent=True,
    #                                                                    ).add(
    #                                 types.KeyboardButton(text="Next")))

    def exit(self):
        print(self.menu_message.chat.id)
        self.bot.telegram_api.edit_message_text(text="new", message_id=self.menu_message.message_id,
                                                        chat_id=self.menu_message.chat.id)
        # self.bot.telegram_api.edit_message_reply_markup(message_id=self.menu_message.message_id,
        #                                                 chat_id=self.menu_message.chat.id)
        # self.bot.remove_reply_menu("View1 Exit", menu=self.menu)
        # self.bot.send_reply_message(message="View1 Exit", reply_markup=types.ReplyKeyboardRemove())

    def handler(self, message: types.Message):
        self.bot.switch_view(next_view=View2)

    @classmethod
    def as_view(cls, bot: Bot):
        cls.as_message_handler(bot=bot)
