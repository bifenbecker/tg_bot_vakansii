from __future__ import annotations
from typing import Optional, TYPE_CHECKING

if TYPE_CHECKING:
    from tools.views import View


class SingletonView:
    _instance: Optional[View] = None

    @classmethod
    def create(cls, *args, **kwargs) -> View:
        """Singleton method of creating instance of view"""
        if cls._instance:
            return cls._instance
        instance = cls(*args, **kwargs)
        cls._instance = instance
        cls.configurate(instance)
        return instance

    @classmethod
    def configurate(cls, instance):
        pass
