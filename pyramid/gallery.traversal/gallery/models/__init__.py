from persistent.mapping import PersistentMapping

class SiteFolder(PersistentMapping):
    __parent__ = None
    __name__ = None

def appmaker(zodb_root):
    if not 'app_root' in zodb_root:
        app_root = MyModel()
        zodb_root['app_root'] = app_root
        import transaction
        transaction.commit()
    return zodb_root['app_root']

from user import *
from album import *
from picture import *
