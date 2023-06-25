from typing import Union
from telebot import types
from .backends import ViewLogicMixin, ViewBotMixin
from tools.middlewares import MiddlewaresType


class View(ViewLogicMixin, ViewBotMixin):
    _handle_obj: Union[types.Message, types.CallbackQuery] = None

    def __init__(self, bot, *args, **kwargs):
        super().__init__(*args, **kwargs)
        ViewBotMixin.__init__(self, bot=bot)

    def pre_handler(self, handle_obj: Union[types.Message, types.CallbackQuery]):
        """Prepare for handler"""
        pass

    def handler(self, handle_obj: Union[types.Message, types.CallbackQuery]):
        """Handler"""
        pass

    def after_handler(self, handle_obj: Union[types.Message, types.CallbackQuery]):
        """Method describe logic after handle message"""
        pass

    def view(self, handle_obj: Union[types.Message, types.CallbackQuery]):
        """Handler ov view"""
        self._handle_obj = handle_obj
        self.bot.user = handle_obj.from_user
        self._run_middlewares(type=MiddlewaresType.BEFORE_HANDLER, handle_obj=handle_obj)
        self._handlers(handle_obj=handle_obj)
        self._run_middlewares(type=MiddlewaresType.AFTER_HANDLER, handle_obj=handle_obj)

    def _handlers(self, handle_obj: Union[types.Message, types.CallbackQuery]):
        self.pre_handler(handle_obj=handle_obj)
        self.handler(handle_obj=handle_obj)
        self.after_handler(handle_obj=handle_obj)

    def as_view(self):
        raise NotImplementedError()
