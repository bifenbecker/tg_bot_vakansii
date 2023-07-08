from telebot import types
from typing import Union, List, Optional, Callable
from tools.views import View
from tools.views.handlers import HandlerMixin


class MultiHandlerView(View, HandlerMixin):
    """
    The Message object also has a content_typeattribute, which defines the type of the Message.
    content_type can be one of the following strings:
        text, audio, document, photo, sticker, video,
        video_note, voice, location, contact, new_chat_members,
        left_chat_member, new_chat_title, new_chat_photo,
        delete_chat_photo, group_chat_created, supergroup_chat_created,
        channel_chat_created, migrate_to_chat_id, migrate_from_chat_id,
        pinned_message, web_app_data
    """

    def __register_file_type_handler(self, file_types: List[str], handler: Callable, *args, **kwargs):
        self._register_handler("register_message_handler", handler,
                               content_types=file_types,
                               *args, **kwargs)

    def __register_message_handler(self, *args, **kwargs):
        self._register_handler("register_message_handler", self._get_message_handler(bot=self.bot),
                               content_types=['text'], *args,
                               **kwargs)

    def __register_callback_handler(self, *args, **kwargs):
        self._register_handler("register_callback_query_handler", self.callback_handler, *args, **kwargs)

    def __register_file_handler(self, file_types: Optional[List[str]] = None, *args, **kwargs):
        if file_types is None:
            file_types = ['document', 'photo', 'audio', 'video']
        self.__register_file_type_handler(file_types=file_types, handler=self.file_handler, *args, **kwargs)

    def __register_document_handler(self, *args, **kwargs):
        self._register_handler("register_message_handler", self.document_handler, content_types=['document'], *args,
                               **kwargs)

    def __register_photo_handler(self, *args, **kwargs):
        self._register_handler("register_message_handler", self.photo_handler, content_types=['photo'], *args, **kwargs)

    def __register_voice_handler(self, *args, **kwargs):
        self._register_handler("register_message_handler", self.voice_handler, content_types=['voice'], *args, **kwargs)

    def __register_contact_handler(self, *args, **kwargs):
        self._register_handler("register_message_handler", self.contact_handler, content_types=['contact'], *args,
                               **kwargs)

    def as_message_handler(self, *args, **kwargs):
        self.__register_message_handler(*args, **kwargs)

    def as_callback_handler(self, *args, **kwargs):
        self.__register_callback_handler(*args, **kwargs)

    def as_file_handler(self, file_types: Optional[List[str]] = None, *args, **kwargs):
        self.__register_file_handler(*args, **kwargs)

    def as_document_handler(self, *args, **kwargs):
        self.__register_document_handler(*args, **kwargs)

    def as_photo_handler(self, *args, **kwargs):
        self.__register_photo_handler(*args, **kwargs)

    def as_voice_handler(self, *args, **kwargs):
        self.__register_voice_handler(*args, **kwargs)

    def as_contact_handler(self, *args, **kwargs):
        self.__register_contact_handler(*args, **kwargs)

# EXAMPLE
# class ExampleView(MultiHandlerView):
#
#     def message_handler(self, message: types.Message):
#         pass
#
#     def callback_handler(self, callback: types.CallbackQuery):
#         pass
#
#      def as_view(self):
#         self.as_message_handler()
#         self.as_callback_handler()
