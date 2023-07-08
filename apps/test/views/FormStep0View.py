from typing import Optional, Union
from telebot import types
from tools.views.form_view import FormView
from tools.views.handlers import MessageHandler
from tools.components import AnsweredMessage
from .FormStep1View import Step1


class Step0(FormView, MessageHandler):

    def entry_render(self, user: types.User, data: Optional[dict] = None):
        self.bot.telegram_api.send_message(chat_id=user.id, text="Введите имя")

    def message_handler(self, message: AnsweredMessage):
        self.form.set_data("name", message.source.text)
        self.form.next_step()

    def handle_errors(self, errors: list):
        print(errors)

    # def process_answer(self, message: types.Message):
    #     self.form.set_data(key="name", value=message.text)
    #     self.bot.switch_view(user=message.from_user, next_view=Step1)
    #
    # def register_view(self):
    #     self._register_handler("register_message_handler", self.process_answer)
