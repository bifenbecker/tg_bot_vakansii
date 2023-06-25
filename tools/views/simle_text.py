from __future__ import annotations
from typing import Optional
from tools.views import View


class SimpleTextView(View):
    """View for render entry text and exit text (optional). Process only(optional) handler"""
    ENTRY_TEXT: str
    EXIT_TEXT: Optional[str] = None

    MIDDLEWARES = {
        View.MiddlewaresType.BEFORE_ENTRY: [
            "entry_render_text"
        ],
        View.MiddlewaresType.BEFORE_EXIT: [
            "exit_render_text"
        ]
    }

    def entry_render_text(self, data):
        self.bot.send_reply_message(text=self.ENTRY_TEXT)

    def exit_render_text(self):
        if self.EXIT_TEXT:
            self.bot.send_reply_message(text=self.EXIT_TEXT)


# EXAMPLE
# class ViewE(SimpleTextView):
#     ENTRY_TEXT = "View 2 entry"
#     EXIT_TEXT = "View 2 exit"
#
#     def handler(self, message: Union[types.Message, types.CallbackQuery]):
#         self.bot.switch_view(next_view=View3)
