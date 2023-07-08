from typing import Union, Optional, Callable
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
        """Common Handler"""
        pass

    def after_handler(self, handle_obj: Union[types.Message, types.CallbackQuery]):
        """Method describe logic after handle message"""
        pass

    def as_view(self, handler: Callable) -> Callable:
        def process_handler(handle_obj: Union[types.Message, types.CallbackQuery], *args, **kwargs):
            self._run_middlewares(type=MiddlewaresType.BEFORE_HANDLER, handle_obj=handle_obj, *args, **kwargs)
            self.pre_handler(handle_obj=handle_obj)
            handler(handle_obj, *args, **kwargs)
            self.after_handler(handle_obj=handle_obj)
            self._run_middlewares(type=MiddlewaresType.AFTER_HANDLER, handle_obj=handle_obj, *args, **kwargs)

        return process_handler

    def view(self, handle_obj: Union[types.Message, types.CallbackQuery]):
        """Handler ov view"""
        self._run_middlewares(type=MiddlewaresType.BEFORE_HANDLER, handle_obj=handle_obj)
        self._handlers(handle_obj=handle_obj)
        self._run_middlewares(type=MiddlewaresType.AFTER_HANDLER, handle_obj=handle_obj)

    def _handlers(self, handle_obj: Union[types.Message, types.CallbackQuery]):
        self.pre_handler(handle_obj=handle_obj)
        self.handler(handle_obj=handle_obj)
        self.after_handler(handle_obj=handle_obj)

    def _register_handler(self, handler_type, callback: Callable, *args, **kwargs):
        if not callback:
            raise Exception("You must provide callback to register handler")

        def filter_message(message: types.Message):
            state_flag = self.bot.current_view(message=message).state_id == self.state
            return state_flag

        if hasattr(self.bot.telegram_api, handler_type):
            register_handler = getattr(self.bot.telegram_api, handler_type)
            register_handler(self.as_view(callback),
                             func=filter_message, *args,
                             **kwargs)

        else:
            raise Exception(f"No such handler type - {handler_type}")

    def register_view(self):
        raise NotImplementedError()
