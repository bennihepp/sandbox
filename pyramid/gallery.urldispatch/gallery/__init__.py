from pyramid.config import Configurator
from sqlalchemy import engine_from_config

from .models import DBSession

def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    config = Configurator(settings=settings)
    engine = engine_from_config(settings, 'sqlalchemy.')
    DBSession.configure(bind=engine)
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('home', '/')
    config.add_route('view_picture', '/albums/{username}/{album_name}/{picture_name}')
    config.add_route('view_album', '/albums/{username}/{album_name}')
    config.add_route('list_albums', '/albums/{username}')
    config.scan()
    return config.make_wsgi_app()
