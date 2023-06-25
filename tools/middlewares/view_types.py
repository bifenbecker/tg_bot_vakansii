from enum import Enum


class MiddlewaresType(Enum):
    BEFORE_HANDLER = "BEFORE_HANDLER"
    AFTER_HANDLER = "BEFORE_HANDLER"
    BEFORE_ENTRY = "BEFORE_ENTRY"
    BEFORE_EXIT = "BEFORE_EXIT"
