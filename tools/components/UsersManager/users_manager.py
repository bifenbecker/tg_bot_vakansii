from __future__ import annotations
from typing import Dict, TYPE_CHECKING, Type, Optional
from tools.components.ViewManager import ViewManager, SimpleViewManager
from tools.views import View
from telebot import types

if TYPE_CHECKING:
    from bot import Bot


class UsersManager:

    def __init__(self, bot: Bot, view_manager_type: Type[ViewManager]):
        self.__users_hash_map: Dict[int, ViewManager] = dict()
        self.bot = bot
        self.__default_view_manager_type = view_manager_type

    @property
    def view_manager(self) -> Type[ViewManager]:
        return self.__default_view_manager_type

    def __create_view_manager_for_user(self, user: types.User, init_view: Optional[Type[View]] = None) -> ViewManager:
        return self.view_manager(bot=self.bot, user=user, init_view=init_view)

    def add_user(self, user: types.User, init_view_for_user: Optional[Type[View]] = None):
        self.__users_hash_map.update({
            user.id: self.__create_view_manager_for_user(user=user, init_view=init_view_for_user)
        })

    def get_view_manager(self, user: types.User) -> ViewManager:
        return self.__users_hash_map[user.id]

    def switch_view_for_user(self, user: types.User, next_view: Type[View], data: Optional[dict] = None,
                             exit_view: bool = True,
                             entry_view: bool = True):
        view_manager_for_user = self.get_view_manager(user=user)
        view_manager_for_user.switch_view(next_view=next_view, data=data, entry_view=entry_view, exit_view=exit_view)

    def back_view_for_user(self, user: types.User, data: Optional[dict] = None,
                           exit_view: bool = True,
                           entry_view: bool = True):
        view_manager_for_user = self.get_view_manager(user=user)
        view_manager_for_user.back_view(data=data, exit_view=exit_view, entry_view=entry_view)

    def current_view_for_user(self, user: types.User) -> Type[View]:
        view_manager_for_user = self.get_view_manager(user=user)
        return view_manager_for_user.current_view
