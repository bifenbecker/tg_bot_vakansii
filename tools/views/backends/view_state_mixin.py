class ViewStateMixin:
    _state_id: int

    def __init__(self, *args, **kwargs):
        self._state_id = id(self)

    @property
    def state(self):
        """State id for switching states"""
        return self._state_id

    @classmethod
    @property
    def state_id(cls):
        return cls._state_id
