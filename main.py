from __future__ import annotations
from tools.exceptions.bot import BotRunException
from core import logger
from core import settings
from bot import Bot


@logger.catch
def main():
    try:
        bot = Bot(token=settings.TG_TOKEN)
        bot.run()
    except BotRunException as error:
        logger.exception(error)
    except Exception:
        raise


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        logger.info("Stop running bot")
    except Exception as e:
        logger.exception(e)
