import transaction

from persistent.mapping import PersistentMapping

class UserDict(PersistentMapping):
    def __init__(self, parent):
        self.__name__ = 'users'
        self.__parnet__ = parent

class User(PersistentMapping):
    def __init__(self, username, parent):
        self.__name__ = username
        self.__parent__ = parent

class UserDictNotFoundException(KeyError):
    pass
class UserNotFoundException(KeyError):
    pass

def retrieve_users(zodb_root, bootstrap=False):
    if 'users' not in zodb_root:
        if bootstrap:
            zodb_root['users'] = UserDict(parent=zodb_root)
            transaction.commit()
        else:
            raise UserDictNotFoundException('User dict does not exist')
    return zodb_root['users']

def retrieve_user(zodb_root, username=None, bootstrap=False):
    if username is None:
        username = '<root>'
    users = retrieve_users(zodb_root, bootstrap=bootstrap)
    if username not in users:
        if bootstrap:
            users[username] = User(username, parent=users)
            transaction.commit()
        else:
            raise UserNotFoundException('User %%%s%% does not exist' % username)
    return users[username]
