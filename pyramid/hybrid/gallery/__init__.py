from pyramid.config import Configurator
from pyramid_zodbconn import get_connection
from pyramid.traversal import model_path, traversal_path

from .models.gallery import retrieve_gallery

def gallery_root_factory(request):
    conn = get_connection(request)
    if 'user' in request.matchdict:
        username = request.matchdicht['user']
        bootstrap = False
    else:
        username = None
        bootstrap = True
    return retrieve_gallery(conn.root(), username, bootstrap=bootstrap)

def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    config = Configurator(settings=settings)
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('home', '/')
    config.add_route('gallery_default', '/gallery/*traverse',
                     factory=gallery_root_factory)
    config.add_route('gallery', '/user/{username}/gallery/*traverse',
                     factory=gallery_root_factory)
    #                 factory=gallery_root_factory, use_global_views=True)
    config.scan()
    return config.make_wsgi_app()
