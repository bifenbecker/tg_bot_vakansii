from __future__ import annotations
from typing import Optional, TYPE_CHECKING, Type, Callable, Union

if TYPE_CHECKING:
    from tools.views import View


class InlineButton:
    text: str
    data: Optional[dict] = None
    callback_data: str
    to_view: Optional[Type[View]] = None
    on_click: Union[Callable, str] = None

    def __init__(self, text: str, callback_data: str, data: Optional[dict] = None, to_view: Optional[Type[View]] = None,
                 on_click: Union[Callable, str] = None):
        self.text = text
        self.callback_data = callback_data
        self.data = data
        self.to_view = to_view
        self.on_click = on_click

    def action(self, switch_view: Callable[[Type[View], bool, Optional[dict]], None], exit_prev: bool = True):
        if self.on_click:
            self.on_click()
        if self.to_view:
            switch_view(self.to_view, exit_prev, self.data)
