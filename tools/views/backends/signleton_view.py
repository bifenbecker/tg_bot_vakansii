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
    @property
    def is_created(cls) -> bool:
        return bool(cls._instance)

    @classmethod
    def get_instance(cls) -> Optional[View]:
        return cls._instance

    @classmethod
    def configurate(cls, instance: View):
        pass
