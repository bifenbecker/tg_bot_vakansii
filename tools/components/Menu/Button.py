from __future__ import annotations
from telebot import types
from typing import Optional, TYPE_CHECKING, Type, Callable, Union

if TYPE_CHECKING:
    from tools.views import View


class Button:
    text: str
    data: Optional[dict] = None
    to_view: Optional[Type[View]] = None
    on_click: Union[Callable, str] = None

    def __init__(self, text: str, data: Optional[dict] = None, to_view: Optional[Type[View]] = None,
                 on_click: Union[Callable, str] = None):
        self.text = text
        self.data = data
        self.to_view = to_view
        self.on_click = on_click

    def action(self, for_user: types.User,
               switch_view: Callable[[types.User, Type[View], bool, Optional[dict], bool], None],
               exit_prev: bool = True, entry_view: bool = True):
        if self.on_click:
            self.on_click()
        if self.to_view:
            switch_view(user=for_user, next_view=self.to_view, exit_view=exit_prev, data_to_next_view=self.data,
                        entry_view=entry_view)
            # switch_view(for_user, self.to_view, exit_prev, self.data, entry_view)
