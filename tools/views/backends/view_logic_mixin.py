from __future__ import annotations
from typing import Optional, TYPE_CHECKING
from .view_state_mixin import ViewStateMixin
from .signleton_view import SingletonView
from tools.middlewares import MiddlewareMixinView, MiddlewaresType

if TYPE_CHECKING:
    from tools.views import View


class ViewLogicMixin(MiddlewareMixinView, ViewStateMixin, SingletonView):
    _prev_view: Optional[View] = None

    def __init__(self, *args, **kwargs):
        ViewStateMixin.__init__(self, *args, **kwargs)
        self._prev_view = None

    @property
    def prev_view(self) -> Optional[View]:
        """Previous view"""
        return self._prev_view

    @prev_view.setter
    def prev_view(self, view: View):
        self._prev_view = view

    def pre_entry(self, data: Optional[dict] = None):
        """Prepare method for entry render"""
        pass

    def entry_render(self, data: Optional[dict] = None):
        """Entry render"""
        pass

    def entry(self, data: Optional[dict] = None):
        """Entry"""
        self._run_middlewares(type=MiddlewaresType.BEFORE_ENTRY, data=data)
        self.pre_entry(data=data)
        self.entry_render(data=data)
        self._run_middlewares(type=MiddlewaresType.AFTER_ENTRY, data=data)

    def exit_render(self):
        """Exit render"""
        pass

    def exit(self):
        """Exit of view"""
        self._run_middlewares(type=MiddlewaresType.BEFORE_EXIT)
        self.exit_render()
        self._run_middlewares(type=MiddlewaresType.AFTER_EXIT)

    @classmethod
    def configurate(cls, instance):
        cls._state_id = instance.state
