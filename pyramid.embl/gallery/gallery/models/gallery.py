import transaction
from persistent.mapping import PersistentMapping

from user import retrieve_user

class Gallery(PersistentMapping):
    __parent__ = None
    __name__ = None

class GalleryNotFoundException(KeyError):
    pass

def retrieve_gallery(zodb_root, username=None, bootstrap=False):
    if username is None:
        username = '<root>'
    user = retrieve_user(zodb_root, username, bootstrap=bootstrap)
    if 'gallery' not in user:
        if bootstrap:
            user['gallery'] = Gallery(parent=user)
            transaction.commit()
        else:
            raise GalleryNotFoundException('User %%%s%% has no gallery' % username)
    return user['gallery']   
