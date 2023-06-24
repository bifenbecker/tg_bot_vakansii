from .base import View
from tools.components import Menu


class MenuView(View):
    IS_REMOVE_MENU_AFTER = True

    def reply_menu(self) -> Menu:
        raise NotImplementedError()

    @property
    def menu(self) -> Menu:
        return self.reply_menu()

    @property
    def text(self) -> str:
        return self.entry_text()

    def entry_text(self) -> str:
        raise NotImplementedError()

    def entry_render(self):
        self.menu_message = self.bot.send_reply_message_with_menu(text=self.text, menu=self.menu)
