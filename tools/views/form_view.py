from __future__ import annotations
from typing import  TYPE_CHECKING
from telebot.types import User
from .base import View

if TYPE_CHECKING:
    from tools.wrappers.forms import BaseForm


class FormView(View):
    # Error pydantic types for handle errors
    # https://docs.pydantic.dev/dev-v2/usage/validation_errors

    form: BaseForm

    def handle_errors(self, errors: list, user: User):
        pass
