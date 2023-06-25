from __future__ import annotations
from bot import Bot


def handler_decorator(type):
    def msg_handler(message):
        print("message")

    def callback_handler(callback):
        print("CALLBACK")
        print(callback)

    config = {
        "message": msg_handler,
        "callback": callback_handler,
    }

    return config.get(type, msg_handler)


def main():
    bot = Bot(token="6153583969:AAHV2N4yv_WkB9iQogDyeXjYKaT4nz1k638")
    bot.run()


if __name__ == '__main__':
    main()
