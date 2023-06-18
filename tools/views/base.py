from __future__ import annotations
from telebot import types
from typing import TYPE_CHECKING, Optional, List, Union

if TYPE_CHECKING:
    from bot import Bot


class View:
    __instance: Optional[View] = None
    bot: Bot
    __state_id: int

    def __init__(self, bot):
        self.bot = bot
        self.__state_id = id(self)

    @property
    def state(self):
        return self.__state_id

    @classmethod
    @property
    def state_id(cls):
        return cls.__state_id

    def pre_entry(self):
        pass

    def entry_render(self):
        pass

    def entry(self):
        self.pre_entry()
        self.entry_render()

    def pre_handler(self, message: Union[types.Message, types.CallbackQuery]):
        pass

    def handler(self, message: Union[types.Message, types.CallbackQuery]):
        pass

    def after_handler(self, message: Union[types.Message, types.CallbackQuery]):
        pass

    def exit(self):
        pass

    def view(self, message: Union[types.Message, types.CallbackQuery]):
        if not self.bot.user:
            self.bot.user = message.from_user
        self.pre_handler(message=message)
        self.handler(message=message)
        self.after_handler(message=message)

    @classmethod
    def create(cls, *args, **kwargs):
        if cls.__instance:
            return cls.__instance
        instance = cls(*args, **kwargs)
        cls.__instance = instance
        cls.__state_id = instance.state
        return instance

    @classmethod
    def as_message_handler(cls, bot: Bot, *args, **kwargs):
        view = cls.create(bot, *args, **kwargs)
        bot.register_message_handler(view.view, func=lambda message: bot.current_view.state_id == view.state)

    @classmethod
    def as_callback_handler(cls, bot: Bot, *args, **kwargs):
        view = cls.create(bot, *args, **kwargs)
        bot.register_callback_handler(view.view, func=lambda message: bot.current_view.state_id == view.state)

    @classmethod
    def as_file_handler(cls, bot: Bot, *args, **kwargs):
        pass

    @classmethod
    def as_command_handler(cls, bot: Bot, commands: List[str], *args, **kwargs):
        view = cls(bot=bot)
        bot.register_message_handler(view.view, commands=commands, *args, **kwargs)

    @classmethod
    def as_view(cls, bot: Bot):
        raise NotImplementedError()
