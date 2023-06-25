from __future__ import annotations
from typing import Union, Optional, TYPE_CHECKING, List, Callable
from telebot import types
from .base_old import View

if TYPE_CHECKING:
    from bot import Bot


class FileView(View):
    """View for handle files. Process only(optional) handler"""
    FILE_TYPES: List[str] = []

    @classmethod
    def as_view(cls, bot: Bot):
        cls.as_file_handler(bot=bot, file_types=cls.FILE_TYPES)


# EXAMPLE
# class ViewE(FileView):
#     FILE_TYPES = ["document"]
#
#     def handler(self, message: Union[types.Message, types.CallbackQuery]):
#         print(message)
