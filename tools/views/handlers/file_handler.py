from typing import List
from .milti_handler import MultiHandlerView


class FileHandler(MultiHandlerView):
    FILE_TYPES: List[str] = []

    def register_view(self):
        self.as_file_handler(file_types=self.FILE_TYPES)
