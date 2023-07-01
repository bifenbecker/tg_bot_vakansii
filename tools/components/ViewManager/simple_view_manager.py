from typing import Optional, Type
from tools.views import View
from .view_manager import ViewManager


class SimpleViewManager(ViewManager):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._prev_view: Optional[Type[View]] = None

    @property
    def prev_view(self) -> Optional[Type[View]]:
        return self._prev_view

    @property
    def prev_view_instance(self) -> Optional[View]:
        return self._prev_view.create(self.bot)

    def switch_view(self, next_view: Type[View], data: Optional[dict] = None, exit_view: bool = True,
                    entry_view: bool = True):
        prev_view = None
        if self._current_view:
            instance = self._current_view.create(self)
            if exit_view:
                instance.exit(user=self.user)
            prev_view = instance
        self._current_view = next_view
        instance = next_view.create(self)
        instance.prev_view = prev_view
        self._prev_view = prev_view.__class__
        if entry_view:
            instance.entry(user=self.user, data=data)

    def back_view(self, data: Optional[dict] = None, exit_view: bool = True, entry_view: bool = True):
        if self._prev_view:
            if exit_view:
                self.prev_view_instance.exit(user=self.user)
            self._current_view = self._prev_view
            if entry_view:
                self.current_view_instance.entry(user=self.user, data=data)
            self._prev_view = None
