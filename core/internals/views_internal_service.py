from __future__ import annotations
from typing import List, Type, TypedDict, TYPE_CHECKING, Optional, Dict
from tools.exceptions.bot import NoLoadedBot
from tools.exceptions.views import EmptyRegisteredViews
from apps.users.models import View as ViewDB
from .import_service import BaseImportService

if TYPE_CHECKING:
    from tools.views import View
    from bot import Bot


class ViewsInternalService(BaseImportService):
    # This class imports models
    # thus it adds them to Base.metadata

    TARGET_FOLDER = "apps"
    TARGET_SUBFOLDERS = "views"
    METADATA_NOT_CHECKED_MESSAGE = "is not checked for metadata (migrations)"
    MODELS_NOT_CHECKED_MESSAGE = "is not checked for models (admin panel)"
    REGISTER_VIEWS_ERROR = "Register views before internals"
    __views: Dict[str, Type[View]] = {}
    __bot: Optional[Bot] = None

    @classmethod
    def get_views(cls) -> List[TypedDict('Module', {'name': str, 'value': Type[View]})]:
        views = cls.get_items(
            target_subfolders=cls.TARGET_SUBFOLDERS,
            not_checked_message=cls.METADATA_NOT_CHECKED_MESSAGE
        )
        return views

    @classmethod
    def __generate_hash_map(cls, views: List[TypedDict('Module', {'name': str, 'value': Type[View]})]):
        for view in views:
            cls.__views.update({
                f"{view['value'].state_id}": view['value']
            })

    @classmethod
    def register_views(cls, bot: Bot):
        views = cls.get_views()
        cls.__bot = bot
        for view_type in views:
            _View: Type[View] = view_type['value']
            instance_view = _View.create(bot)
            instance_view.register_view()

        cls.__generate_hash_map(views=views)

    @classmethod
    def get_view_class(cls, hash_string: str) -> Optional[Type[View]]:
        return cls.__views.get(hash_string, None)

    @classmethod
    def parse_db_objects(cls, db_views: List[ViewDB]) -> List[Type[View]]:
        pass
