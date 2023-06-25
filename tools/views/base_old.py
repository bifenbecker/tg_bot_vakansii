from __future__ import annotations
from telebot import types
from typing import TYPE_CHECKING, Optional, List, Union, Callable, Dict
from .handlers import HandlerMixin
from tools.middlewares import MiddlewaresType, MiddlewareMixinView

if TYPE_CHECKING:
    from bot import Bot


class View(MiddlewareMixinView, HandlerMixin):
    """
    Base View class
    """

    __instance: Optional[View] = None
    __state_id: int
    _prev_view: Optional[View] = None
    _message: Union[types.Message, types.CallbackQuery] = None
    bot: Bot

    def __init__(self, bot):
        self.bot = bot
        self.__state_id = id(self)
        self._prev_view = None

    @property
    def state(self):
        """State id for switching states"""
        return self.__state_id

    @property
    def prev_view(self) -> Optional[View]:
        """Previous view"""
        return self._prev_view

    @prev_view.setter
    def prev_view(self, view: View):
        self._prev_view = view

    def pre_entry(self, data: Optional[dict] = None):
        """Prepare method for entry render"""
        pass

    def entry_render(self, data: Optional[dict] = None):
        """Entry render"""
        pass

    def entry(self, data: Optional[dict] = None):
        """Entry"""
        self._run_middlewares(type=MiddlewaresType.BEFORE_ENTRY, data=data)
        self.pre_entry(data=data)
        self.entry_render(data=data)

    def pre_handler(self, message: Union[types.Message, types.CallbackQuery]):
        """Prepare for handler"""
        pass

    def handler(self, message: Union[types.Message, types.CallbackQuery]):
        """Handler"""
        pass

    def after_handler(self, message: Union[types.Message, types.CallbackQuery]):
        """Method describe logic after handle message"""
        pass

    def exit_render(self):
        """Exit render"""
        pass

    def exit(self):
        """Exit of view"""
        self._run_middlewares(type=MiddlewaresType.BEFORE_EXIT)
        self.exit_render()

    def view_decorator(self, type):
        handlers = {
            "message": self.message_handler,
            "callback": self.callback_handler,
        }

    def view(self, message: Union[types.Message, types.CallbackQuery]):
        """Handler ov view"""
        self.bot.user = message.from_user
        self._message = message
        self._run_middlewares(type=MiddlewaresType.BEFORE_HANDLER, message=message)
        self._handlers(message=message)
        self._run_middlewares(type=MiddlewaresType.AFTER_HANDLER, message=message)

    @classmethod
    @property
    def state_id(cls):
        return cls.__state_id

    @classmethod
    def create(cls, *args, **kwargs):
        """Singleton method of creating instance of view"""
        if cls.__instance:
            return cls.__instance
        instance = cls(*args, **kwargs)
        cls.__instance = instance
        cls.__state_id = instance.state
        return instance

    @classmethod
    def as_message_handler(cls, bot: Bot, *args, **kwargs):
        view = cls.create(bot, *args, **kwargs)
        bot.telegram_api.register_message_handler(view.view,
                                                  func=lambda message: bot.current_view.state_id == view.state)

    @classmethod
    def as_callback_handler(cls, bot: Bot, *args, **kwargs):
        view = cls.create(bot, *args, **kwargs)
        bot.telegram_api.register_callback_query_handler(view.view,
                                                         func=lambda message: bot.current_view.state_id == view.state)

    @classmethod
    def as_file_handler(cls, bot: Bot, file_types: Optional[List[str]] = None, *args, **kwargs):
        if file_types is None:
            file_types = ['document', 'photo']
        view = cls.create(bot, *args, **kwargs)
        bot.telegram_api.register_message_handler(view.view,
                                                  func=lambda message: bot.current_view.state_id == view.state,
                                                  content_types=file_types)

    @classmethod
    def as_command_handler(cls, bot: Bot, commands: List[str], *args, **kwargs):
        view = cls(bot=bot)
        bot.telegram_api.register_message_handler(view.view, commands=commands, *args, **kwargs)

    @classmethod
    def as_view(cls, bot: Bot):
        raise NotImplementedError()

    def _handlers(self, message: Union[types.Message, types.CallbackQuery]):
        self.pre_handler(message=message)
        self.handler(message=message)
        self.after_handler(message=message)
