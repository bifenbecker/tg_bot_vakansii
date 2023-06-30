from typing import *
from .view_types import MiddlewaresType


class MiddlewaresMeta(type):
    def __new__(cls, name, bases, attrs):
        collected_middlewares: Dict[MiddlewaresType, List[Callable]] = {}

        for base in bases:
            if hasattr(base, 'MIDDLEWARES'):
                sub_middlewares = getattr(base, 'MIDDLEWARES')
                for middleware_type, typed_middlewares in sub_middlewares.items():
                    if typed_collected_middlewares := collected_middlewares.get(middleware_type):
                        typed_collected_middlewares.extend(typed_middlewares)
                    else:
                        collected_middlewares.update({
                            middleware_type: typed_middlewares
                        })
        if not attrs.get('MIDDLEWARES'):
            attrs.update({
                'MIDDLEWARES': collected_middlewares
            })
            return super().__new__(cls, name, bases, attrs)
        for middleware_type, typed_middlewares in collected_middlewares.items():
            if typed_collected_middlewares := attrs['MIDDLEWARES'].get(middleware_type):
                for middleware in typed_middlewares[::-1]:
                    typed_collected_middlewares.insert(0, middleware)
            else:
                attrs['MIDDLEWARES'].update({
                    middleware_type: typed_middlewares
                })
        return super().__new__(cls, name, bases, attrs)
