from typing import Union, Type, TYPE_CHECKING, Optional
from telebot import types
from .base import View

if TYPE_CHECKING:
    from bot import Bot


class AnswerView(View):
    NEXT_VIEW: Type[View]
    ERROR_MESSAGE: Optional[str] = "Enter valid data"
    SUCCESS_MESSAGE: Optional[str] = None
    REPEAT_RENDER: bool = False
    IS_SHOWED_RENDER: bool = False
    SHOW_ERROR_AFTER_RENDER: bool = True
    ANSWER_COUNT: int = 0

    def process_answer(self, message: Union[types.Message, types.CallbackQuery]) -> bool:
        return False

    def switch_view(self):
        self.bot.switch_view(next_view=self.NEXT_VIEW)

    def check_answer(self, message: Union[types.Message, types.CallbackQuery]):
        if self.process_answer(message=message):
            self.switch_view()
        else:
            self.bot.send_message(to=self.bot.user.id, message=self.ERROR_MESSAGE)

    def view(self, message: Union[types.Message, types.CallbackQuery]):
        self.ANSWER_COUNT += 1
        if not self.bot.user:
            self.bot.user = message.from_user

        if self.ANSWER_COUNT < 2:
            super().view(message=message)
            self.IS_SHOWED_RENDER = True
        else:
            is_valid_answer = self.process_answer(message=message)
            if is_valid_answer:
                if self.SUCCESS_MESSAGE:
                    self.bot.send_message(to=self.bot.user.id, message=self.SUCCESS_MESSAGE)
                self.switch_view()
            else:
                if self.REPEAT_RENDER or self.ERROR_MESSAGE:
                    if self.SHOW_ERROR_AFTER_RENDER:
                        if self.REPEAT_RENDER:
                            self.render(message=message)
                        if self.ERROR_MESSAGE:
                            self.bot.send_message(to=self.bot.user.id, message=self.ERROR_MESSAGE)
                    else:
                        if self.ERROR_MESSAGE:
                            self.bot.send_message(to=self.bot.user.id, message=self.ERROR_MESSAGE)
                        if self.REPEAT_RENDER:
                            self.render(message=message)
