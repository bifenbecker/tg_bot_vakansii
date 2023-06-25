from typing import Optional
from telebot import types
from tools.components import Menu
from tools.views import View


# class MenuView(View):
class MenuView(View):
    """Add reply keyboard menu for view"""
    IS_REMOVE_MENU_AFTER = True
    MENU: Optional[Menu] = None
    TEXT_FOR_MENU: str

    MIDDLEWARES = {
        View.MiddlewaresType.BEFORE_ENTRY: [
            "upload_bot_to_menu",
            "render_entry_menu"
        ],
        View.MiddlewaresType.AFTER_HANDLER: [
            "on_switch_next_view_menu",
        ]
    }

    def upload_bot_to_menu(self, data: Optional[dict] = None):
        self.MENU.bot = self.bot

    def render_entry_menu(self, data: Optional[dict] = None):
        self.menu_message = self.bot.send_reply_message_with_menu(text=self.TEXT_FOR_MENU, menu=self.MENU)

    def on_switch_next_view_menu(self, message: types.Message):
        for button in self.MENU.buttons:
            if button.text == message.text:
                if button.to_view:
                    self.bot.switch_view(next_view=button.to_view, data_to_next_view=button.data)

    def exit(self):
        if self.IS_REMOVE_MENU_AFTER:
            self.bot.remove_menu(menu=self.MENU)

# Example
# class View1(MessageHandler, MenuView):
#     TEXT_FOR_MENU = "Hello"
#     MENU = Menu(
#         Button("btn1")
#     )
#
#     def message_handler(self, message: types.Message):
#         print(message)
