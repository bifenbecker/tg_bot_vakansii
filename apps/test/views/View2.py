from telebot import types
from tools.views import SimpleTextView
from tools.views.handlers import MessageHandler


class View2(SimpleTextView, MessageHandler):
    ENTRY_TEXT = "View2"

    def message_handler(self, message: types.Message):
        self.bot.back_view(user=message.from_user, exit_view=False)
