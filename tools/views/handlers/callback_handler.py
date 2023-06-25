from .milti_handler import MultiHandlerView


class CallbackHandler(MultiHandlerView):

    def as_view(self):
        self.bot.telegram_api.register_callback_query_handler(self.callback_handler,
                                                              func=lambda
                                                                  callback: self.bot.current_view.state_id == self.state)
