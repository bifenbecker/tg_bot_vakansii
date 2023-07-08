from __future__ import annotations
from telebot import types
from abc import ABC, abstractmethod
from typing import Optional, Type, TYPE_CHECKING, Dict
from tools.views import View

if TYPE_CHECKING:
    from bot import Bot


class ViewManager(ABC):

    def __init__(self, bot: Bot, user: Optional[types.User] = None, init_view: Optional[Type[View]] = None, *args,
                 **kwargs):
        self.bot = bot
        self.user: Optional[types.User] = user
        self._current_view: Type[View] = init_view

    def _get_current_view(self) -> Type[View]:
        return self._current_view

    @property
    def current_view(self) -> Type[View]:
        return self._get_current_view()

    def create_view_instance(self, *args, **kwargs):
        self.current_view.create(*args, **kwargs)

    @property
    def current_view_instance(self) -> View:
        return self.current_view.get_instance()

    @abstractmethod
    def switch_view(self, next_view: Type[View], data: Optional[dict] = None, exit_view: bool = True,
                    entry_view: bool = True, *args, **kwargs):
        pass

    @abstractmethod
    def back_view(self, data: Optional[dict] = None, exit_view: bool = True, entry_view: bool = True):
        pass

    @classmethod
    def fabric(cls, view_manager_type: Type[ViewManager], *args, **kwargs) -> ViewManager:
        return view_manager_type(*args, **kwargs)
