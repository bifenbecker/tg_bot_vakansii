from telebot import types


class HandlerMixin:

    def message_handler(self, message: types.Message):
        pass

    def callback_handler(self, callback: types.CallbackQuery):
        pass

    def file_handler(self, message: types.Message):
        pass

    def document_handler(self, message: types.Message):
        pass

    def photo_handler(self, message: types.Message):
        pass

    def voice_handler(self, message: types.Message):
        pass

    def contact_handler(self, message: types.Message):
        pass
