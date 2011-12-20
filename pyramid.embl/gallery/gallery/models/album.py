import datetime

from persistent import Persistent
from persistent.mapping import PersistentMapping

class Album(Persistent):
    def __init__(self, name, description=None, location=None,
                 date=datetime.datetime.now(),
                 pictures=PersistentMapping(), parent=None):
        self.__name__ = name
        self.__parent__ = parent
        self.description = description
        self.location = location
        self.date = date
        self.pictures = pictures
