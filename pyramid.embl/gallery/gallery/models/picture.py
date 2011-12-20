import datetime

from persistent import Persistent
from persistent.mapping import PersistentMapping

class Picture(Persistent):
    def __init__(self, name, display_url, original_url=None,
                 thumbnail_url=None, description=None,
                 location=None, date=datetime.datetime.now(),
                 parent=None):
        self.__name__ = name
        self.__parent__ = parent
        self.display_url = display_url
        self.original_url = original_url
        self.thumbnail_url = thumbnail_url
        self.description = description
        self.location = location
        self.date = date
