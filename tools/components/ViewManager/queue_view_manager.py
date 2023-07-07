import queue
from typing import Optional, Type, List
from tools.views import View
from .view_manager import ViewManager


class QueueViewManager(ViewManager):

    def __init__(self, max_len: int, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._queue: queue.LifoQueue[Type[View]] = queue.LifoQueue(maxsize=max_len)
        if self._current_view:
            self._queue.put(item=self._current_view)

    @property
    def current_view(self) -> Optional[Type[View]]:
        if not self._queue.empty():
            return self._queue.queue[-1]

    @property
    def current_view_instance(self) -> View:
        return self._queue.queue[-1].create(self.bot)

    @property
    def list_views(self) -> List[Type[View]]:
        return self._queue.queue

    def switch_view(self, next_view: Type[View], data: Optional[dict] = None, exit_view: bool = True, entry_view: bool = True):
        prev_view = None
        if self.current_view:
            prev_view = self.current_view_instance
            if exit_view:
                self.current_view_instance.exit(user=self.user)
        self._queue.put(item=next_view)
        self.current_view_instance.prev_view = prev_view
        if entry_view:
            self.current_view_instance.entry(user=self.user, data=data)

    def back_view(self, data: Optional[dict] = None, exit_view: bool = True, entry_view: bool = True):
        view = self._queue.get().create(self.bot)
        if exit_view:
            view.exit(user=self.user)
        if entry_view:
            self.current_view_instance.entry(user=self.user, data=data)

