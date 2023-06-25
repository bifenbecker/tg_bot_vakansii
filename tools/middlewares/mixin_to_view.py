from typing import *
from .metaclass import MiddlewaresMeta
from .view_types import MiddlewaresType


class MiddlewareMixinView(metaclass=MiddlewaresMeta):
    MIDDLEWARES: Dict[MiddlewaresType, List[str]] = {}
    MiddlewaresType = MiddlewaresType

    def _run_middlewares(self, type: MiddlewaresType, *args, **kwargs):
        if str_middlewares := self.MIDDLEWARES.get(type, None):
            middlewares = [getattr(self, str_name) for str_name in str_middlewares]
            for middleware in middlewares:
                middleware(*args, **kwargs)
