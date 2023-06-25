from .milti_handler import MultiHandlerView


class MessageHandler(MultiHandlerView):

    def as_view(self):
        self.bot.telegram_api.register_message_handler(self.message_handler,
                                                       func=lambda
                                                           message: self.bot.current_view.state_id == self.state)
