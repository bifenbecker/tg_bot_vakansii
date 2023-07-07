import sys
from core.configuration import settings
from loguru import logger

logger.remove()

logger.add(
    sys.stderr,
    level=settings.LOG_LEVEL,
    backtrace=settings.LOGURU_BACKTRACE,
    diagnose=settings.LOGURU_DIAGNOSE,
)
