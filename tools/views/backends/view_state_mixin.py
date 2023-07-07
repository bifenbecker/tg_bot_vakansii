from typing import Optional
from _hashlib import HASH
from hashlib import sha1


class ViewStateMixin:
    __viewname__: Optional[str] = None
    _state_id: str
    __hash_obj: HASH

    def __init__(self, hash_method: Optional[HASH] = sha1(), *args, **kwargs):
        self.__hash_obj = hash_method
        self.__hash_obj.update(self.__viewname__ or self.__class__.__name__.encode("utf-8"))
        self._state_id = self.__hash_obj.hexdigest()

    @property
    def hash_obj(self) -> HASH:
        return self.__hash_obj

    @property
    def state(self) -> str:
        """State id for switching states"""
        return self._state_id

    @classmethod
    @property
    def state_id(cls) -> str:
        return cls._state_id

    @classmethod
    @property
    def hash_obj_cls(cls) -> HASH:
        return cls.__hash_obj
