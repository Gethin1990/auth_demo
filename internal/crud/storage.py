class Storage(object):
    _storage = dict()
    def __init__(self):
        self._storage = Storage.__CACHE

    def __new__(cls, *args, **kwargs):

        if not hasattr(Storage, "_instance"):
            with Storage.__instance_lock:
                if not hasattr(Storage, "_instance"):
                    Storage._instance = object.__new__(cls)
        return Storage._instance

