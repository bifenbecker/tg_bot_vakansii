from typing import Optional
from telebot import types
from tools.views.form_view import FormView


class Step1(FormView):

    def entry_render(self, user: types.User, data: Optional[dict] = None):
        self.bot.telegram_api.send_message(chat_id=user.id, text="Введите возраст")

    def process_answer(self, message: types.Message):
        self.form.set_data(key="age", value=message.text)
        self.form.next_step()

    def handle_errors(self, errors: list, user: types.User):
        if errors[0]['type'] == "int_parsing":
            self.bot.telegram_api.send_message(chat_id=user.id, text="Введите число")

    def register_view(self):
        self._register_handler("register_message_handler", self.process_answer)
