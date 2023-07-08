from __future__ import annotations
from typing import TYPE_CHECKING, Union, Optional, List
from telebot import types
from tools.views import CallbackView, View, SimpleTextView, MenuView, PaginatedCallbackView
from tools.components import Menu, Button, InlineKeyboard, InlineButton, AnsweredMessage
from tools.views.handlers import MessageHandler, CallbackHandler, MultiHandlerView
from core import logger
from .View2 import View2

if TYPE_CHECKING:
    from bot import Bot


class View1(MessageHandler):

    def message_handler(self, message: AnsweredMessage):
        message.answer(text="Hello")
