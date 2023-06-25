from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from bot import Bot


# Maybe it will be deleted when DI integrated
class ViewBotMixin:
    bot: Bot

    def __init__(self, bot: Bot):
        self.bot = bot
