class Singleton(object):
    instance = None

    def __new__(class_, *args, **kwargs):
        if not isinstance(class_.instance, class_):
            instance = super().__new__(*args, **kwargs)
            class_.instance = instance
        return class_.instance
