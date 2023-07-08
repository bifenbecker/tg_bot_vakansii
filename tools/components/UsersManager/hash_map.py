from __future__ import annotations
from typing import Dict, Type, Optional
from tools.components.ViewManager import ViewManager
from tools.views import View
from telebot import types
from .base import BaseUsersManager


class HashMapUsersManager(BaseUsersManager):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__users_hash_map: Dict[int, ViewManager] = dict()

    def get_view_manager(self, user: types.User) -> ViewManager:
        return self.__users_hash_map[user.id]

    def add_user(self, user: types.User, init_view_for_user: Optional[Type[View]] = None):
        self.__users_hash_map.update({
            user.id: self._create_view_manager_for_user(user=user, init_view=init_view_for_user)
        })

