from persistent import Persistent
from persistent.mapping import PersistentMapping

class User(Persistent):
    def __init__(self, name, email, password_hash,
                 albums=PersistentMapping(), parent=None):
        self.__name__ = name
        self.__parent__ = parent
        self.email = email
        self.password_hash = password_hash
        self.albums = albums
