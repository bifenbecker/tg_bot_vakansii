from .milti_handler import MultiHandlerView


class CallbackHandler(MultiHandlerView):

    def register_view(self):
        self.as_callback_handler()
