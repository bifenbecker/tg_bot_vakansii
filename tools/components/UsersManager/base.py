from __future__ import annotations
from abc import ABC, abstractmethod
from telebot import types
from typing import Type, TYPE_CHECKING, Optional
from tools.views import View
from tools.components import ViewManager

if TYPE_CHECKING:
    from bot import Bot


class BaseUsersManager(ABC):

    def __init__(self, bot: Bot, view_manager_type: Type[ViewManager]):
        self.bot: Bot = bot
        self.__default_view_manager_type: Type[ViewManager] = view_manager_type

    @property
    def view_manager(self) -> Type[ViewManager]:
        return self.__default_view_manager_type

    def _create_view_manager_for_user(self, user: types.User, init_view: Optional[Type[View]] = None, *args,
                                      **kwargs) -> ViewManager:
        return self.view_manager(bot=self.bot, user=user, init_view=init_view, *args, **kwargs)

    @abstractmethod
    def get_view_manager(self, user: types.User) -> ViewManager:
        pass

    @abstractmethod
    def add_user(self, user: types.User, init_view_for_user: Optional[Type[View]] = None):
        pass

    def switch_view_for_user(self, user: types.User, next_view: Type[View], data: Optional[dict] = None,
                             exit_view: bool = True,
                             entry_view: bool = True, *args, **kwargs):
        view_manager_for_user = self.get_view_manager(user=user)
        view_manager_for_user.switch_view(next_view=next_view, data=data, entry_view=entry_view, exit_view=exit_view,
                                          *args, **kwargs)

    def back_view_for_user(self, user: types.User, data: Optional[dict] = None,
                           exit_view: bool = True,
                           entry_view: bool = True):
        view_manager_for_user = self.get_view_manager(user=user)
        view_manager_for_user.back_view(data=data, exit_view=exit_view, entry_view=entry_view)

    def current_view_for_user(self, user: types.User) -> Type[View]:
        view_manager_for_user = self.get_view_manager(user=user)
        return view_manager_for_user.current_view
