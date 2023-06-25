from __future__ import annotations
from typing import Optional, TYPE_CHECKING, Type, Callable

if TYPE_CHECKING:
    from tools.views import View


class Button:
    text: str
    data: Optional[dict] = None
    to_view: Optional[Type[View]] = None
    on_click: Optional[Callable] = None

    def __init__(self, text: str, data: Optional[dict] = None, to_view: Optional[Type[View]] = None,
                 on_click: Optional[Callable] = None):
        self.text = text
        self.data = data
        self.to_view = to_view
        self.on_click = on_click

    def action(self, switch_view: Callable[[Type[View], bool, Optional[dict]], None], exit_prev: bool = True):
        if self.on_click:
            self.on_click()
        if self.to_view:
            switch_view(self.to_view, exit_prev, self.data)
