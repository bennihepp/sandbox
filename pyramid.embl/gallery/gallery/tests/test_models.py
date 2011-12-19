import unittest
import transaction

from pyramid import testing

from ..models import (
    DBSession,
    Base,
    UserModel,
    AlbumModel,
    PictureModel,
    )

class TestModels(unittest.TestCase):

    def setUp(self):
        self.config = testing.setUp()
        from sqlalchemy import create_engine
        from sqlalchemy.orm import sessionmaker
        engine = create_engine('sqlite:///:memory:')
        DBSession.configure(bind=engine)
        from zope.sqlalchemy import ZopeTransactionExtension
        Base.metadata.create_all(engine)
        with transaction.manager:
            from ..scripts.populate import fillDB
            fillDB(DBSession())

    def tearDown(self):
        DBSession.remove()
        testing.tearDown()

    def test_UserModel(self):
        pass
    
    def test_AlbumModel(self):
        pass

    def test_PictureModel(self):
        pass

def run():
    unittest.main()

if __name__ == '__main__':
    run()

