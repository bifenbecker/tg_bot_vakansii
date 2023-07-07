from __future__ import annotations
from telebot import types
from sqlalchemy.orm import Session
from typing import Type, Optional, TYPE_CHECKING
from core import ViewsInternalService
from tools.views import View
from tools.components.ViewManager.database_view_manager import DatabaseViewManager
from db import SyncSession
from apps.users.models import ViewHistory, View as ViewDB
from .base import BaseUsersManager

if TYPE_CHECKING:
    from bot import Bot


class DatabaseUsersManager(BaseUsersManager):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.db_conn: Session = SyncSession()
        self._view_manager = None

    def get_view_manager(self, user: types.User) -> DatabaseViewManager:
        with self.db_conn as session:
            history = session.query(ViewHistory).filter_by(user_id=user.id).one_or_none()
        if not history:
            raise Exception("Create history for user before invoke")
        return DatabaseViewManager(bot=self.bot, user=user, db_conn=self.db_conn, history_id=history.id)

    def add_user(self, user: types.User, init_view_for_user: Optional[Type[View]] = None):
        with self.db_conn as session:
            if not session.query(ViewHistory).filter_by(user_id=user.id).one_or_none():
                user_history = ViewHistory(
                    user_id=user.id
                )
                if init_view_for_user:
                    first_view_for_user = ViewDB(
                        history=user_history,
                        name=init_view_for_user.__name__,
                        view_id=init_view_for_user.state_id
                    )
                    session.add(first_view_for_user)

                session.add(user_history)
                session.commit()
