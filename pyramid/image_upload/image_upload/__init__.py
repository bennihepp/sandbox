from pyramid.config import Configurator
from sqlalchemy import engine_from_config

from .models import DBSession

def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    engine = engine_from_config(settings, 'sqlalchemy.')
    DBSession.configure(bind=engine)
    config = Configurator(settings=settings)
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_static_view('javascript', 'javascript', cache_max_age=3600)
    config.add_route('home', '/')
    config.add_route('file_selector', '/file_selector')
    config.add_route('upload', '/upload')
    config.scan()
    return config.make_wsgi_app()

