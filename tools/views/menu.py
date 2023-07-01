from typing import Optional
from telebot import types
from tools.components import Menu
from tools.views import View


class MenuView(View):
    """Add reply keyboard menu for view"""

    MIDDLEWARES = {
        View.MiddlewaresType.BEFORE_ENTRY: [
            "preprocess_buttons",
            "render_entry_menu"
        ],
        View.MiddlewaresType.AFTER_HANDLER: [
            "on_click_button_menu",
        ],
    }

    def preprocess_buttons(self, user: types.User, data: Optional[dict] = None):
        for button in self.configure_menu(user=user).buttons:
            if str_on_click_handler := button.on_click:
                if hasattr(self, str_on_click_handler):
                    func_on_click_handler = getattr(self, str_on_click_handler)
                    button.on_click = func_on_click_handler
                else:
                    raise Exception("No such handler for button")

    def configure_menu(self, user: types.User) -> Menu:
        raise NotImplementedError()

    def text_for_menu(self, user: types.User) -> str:
        raise NotImplementedError()

    def render_entry_menu(self, user: types.User, data: Optional[dict] = None):
        self.menu_message = self.bot.send_message_with_menu(chat_id=user.id, text=self.text_for_menu(user=user),
                                                            menu=self.configure_menu(user=user))

    def on_click_button_menu(self, handle_obj: types.Message):
        menu = self.configure_menu(user=handle_obj.from_user)
        for button in menu.buttons:
            if button.text == handle_obj.text:
                menu.action(button=button)

# Example
# class View1(MessageHandler, MenuView):
#     def configure_menu(self, user: types.User) -> Menu:
#         menu = Menu(
#             Button("Test", to_view=View2)
#         ).options(
#             user=user,
#             bot=self.bot
#         )
#         return menu
#
#     def text_for_menu(self, user: types.User) -> str:
#         return "Test"
#
#     def message_handler(self, message: types.Message):
#         print(message)
