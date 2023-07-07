from __future__ import annotations
from sqlalchemy.orm import Session
from typing import Type, Optional, List
from core.internals.views_internal_service import ViewsInternalService
from tools.views import View
from apps.users.models import ViewHistory, View as ViewDB
from .view_manager import ViewManager


class DatabaseViewManager(ViewManager):
    def __init__(self, history_id: int, db_conn: Optional[Session] = None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.history_id = history_id
        self.db_conn: Session = db_conn

    def __current_view_query(self) -> Optional[ViewDB]:
        """
        Make query to database and return view if it exists
        :return: view object from database - View
        :rtype: View
        """
        with self.db_conn as session:
            view_history_of_user = session.query(ViewHistory).filter_by(user_id=self.user.id).one_or_none()
            if not view_history_of_user:
                return None
            if len(view_history_of_user.views) > 0:
                return view_history_of_user.views[-1]

    @property
    def current_view(self) -> Optional[Type[View]]:
        if not self.db_conn:
            raise Exception("Initialize db connection before")

        if view_from_db := self.__current_view_query():
            return ViewsInternalService.get_view_class(hash_string=view_from_db.view_hash)

    @property
    def current_view_instance(self) -> Optional[View]:
        if not self.db_conn:
            raise Exception("Initialize db connection before")
        if self.current_view:
            return self.current_view.create(self.bot)

    @property
    def list_views(self) -> List[Type[View]]:
        raise NotImplementedError()

    def switch_view(self, next_view: Type[View], data: Optional[dict] = None, exit_view: bool = True,
                    entry_view: bool = True):
        prev_view = None
        if self.current_view:
            prev_view = self.current_view_instance
            if exit_view:
                self.current_view_instance.exit(user=self.user)
        if not self.db_conn:
            raise Exception("Initialize db connection before")
        with self.db_conn as session:
            view = ViewDB(
                history_id=self.history_id,
                name=next_view.__name__,
                view_hash=next_view.state_id
            )
            session.add(view)
            session.commit()
        self.current_view_instance.prev_view = prev_view
        if entry_view:
            self.current_view_instance.entry(user=self.user, data=data)

    def back_view(self, data: Optional[dict] = None, exit_view: bool = True, entry_view: bool = True):
        if exit_view:
            self.current_view_instance.exit(user=self.user)
        current_view_from_db = self.__current_view_query()
        with self.db_conn as session:
            session.delete(current_view_from_db)
            session.commit()
        if entry_view:
            self.current_view_instance.entry(user=self.user, data=data)
