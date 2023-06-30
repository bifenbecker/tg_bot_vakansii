from .milti_handler import MultiHandlerView


class MessageHandler(MultiHandlerView):

    def register_view(self):
        self.as_message_handler()
