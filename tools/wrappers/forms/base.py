from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List, TYPE_CHECKING, Type, Optional
from telebot.storage import StateStorageBase
from telebot.types import User
from pydantic import BaseModel, ValidationError
from core import logger

if TYPE_CHECKING:
    from bot import Bot
    from tools.views.form_view import FormView


class State:
    def __init__(self, name: str):
        self.name = name


class BaseForm(ABC):
    VIEWS: List[Type[FormView]] = []
    Schema: Optional[Type[BaseModel]] = None

    def __init__(self, storage: StateStorageBase, bot: Bot, user: User):
        self._bot = bot
        self._user = user
        self._storage = storage
        self.step = 0
        for View in self.VIEWS:
            state = State(name=View.state_id)
            self._storage.set_state(chat_id=self._user.id, user_id=self._user.id, state=state)
            View.form = self
        if not self.Schema:
            raise Exception("Initialize schema before initialize form")

    @property
    def current_view_step(self) -> Type[FormView]:
        return self.VIEWS[self.step]

    @property
    def current_view_step_instance(self) -> Optional[FormView]:
        return self.current_view_step.get_instance()

    @property
    def data(self) -> dict:
        return self.storage.get_data(chat_id=self._user.id, user_id=self._user.id)

    def _validate(self, exception: bool = True) -> bool:
        try:
            self.Schema.model_validate(self.data)
            return True
        except ValidationError as exc:
            if exception:
                raise exc

    def next_step(self):
        try:
            logger.info(self.data)
            self.Schema.model_validate(self.data)
        except ValidationError as e:
            if self.current_view_step_instance:
                self.current_view_step_instance.handle_errors(errors=e.errors(), user=self._user)
        else:
            if self.step + 1 > len(self.VIEWS) - 1:
                self.exit()
            else:
                self.step += 1
                self._bot.switch_view(user=self._user, next_view=self.VIEWS[self.step])

    def entry(self):
        self._bot.switch_view(user=self._user, next_view=self.VIEWS[self.step])

    def exit(self):
        obj = self.Schema(**self.data)
        logger.info(f"EXIT {obj}")

    @property
    def storage(self) -> StateStorageBase:
        return self._storage

    @abstractmethod
    def save_data(self):
        raise NotImplemented()

    def reset_storage(self, chat_id: int, user_id: int):
        self._storage.reset_data(chat_id, user_id)

    def set_data(self, key: str, value: str, chat_id: Optional[int] = None):
        if not chat_id:
            chat_id = self._user.id
        self._storage.set_data(chat_id, self._user.id, key, value)
