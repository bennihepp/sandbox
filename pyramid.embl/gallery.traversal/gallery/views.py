from pyramid.view import view_config
from .models import MyModel

@view_config(context=MyModel, renderer='templates/mytemplate.pt')
def my_view(request):
    return {'project':'gallery'}

from pyramid.view import view_config
from pyramid.httpexceptions import (
    HTTPFound,
    HTTPNotFound,
    HTTPForbidden,
)

from .models import (
    SiteRoot,
    User,
    Album,
    Picture,
)

@view_config(context=SiteRoot)
def root(context, request):
    return HTTPFound(location=request.resource_url('list_albums', username='hepp'))

@view_config(route_name='list_albums', renderer='list_albums.mako')
def list_albums(request):
    #one = DBSession.query(MyModel).filter(MyModel.name=='one').first()
    username = request.matchdict['username']
    user = DBSession.query(UserModel).\
        filter(UserModel.name == username).\
        first()
    albums = user.albums
    #albums = DBSession.query(AlbumModel).join(UserModel).\
    #    filter(AlbumModel.user_id == UserModel.id).\
    #    filter(UserModel.name == username).\
    #    all()
    def album_href(album):
        href = request.route_url('view_album',
                                 #username=username,
                                 album_name=album.name,
                                 **request.matchdict)
        return href

    return {'username' : username, 'albums' : albums, 'album_href' : album_href}

@view_config(route_name='view_album', renderer='view_album.mako')
def view_album(request):
    username, album_name = request.matchdict['username'], request.matchdict['album_name']
    user = DBSession.query(UserModel).\
        filter(UserModel.name == username).\
        first()
    album = user.albums[album_name]
    #album = DBSession.query(AlbumModel).join(UserModel).\
    #    filter(AlbumModel.name == album_name).\
    #    filter(AlbumModel.user_id == UserModel.id).\
    #    filter(UserModel.name == username).\
    #    first()
    pictures = album.pictures
    #pictures = DBSession.query(PictureModel).\
    #    filter(PictureModel.album_id == album.id).\
    #    all()
    def picture_href(picture):
        href = request.route_url('view_picture',
                                 #username=username,
                                 #album_name=album_name,
                                 picture_name=picture.name,
                                 **request.matchdict)
        return href

    return {'username' : username, 'album' : album, 'pictures' : pictures, 'picture_href' : picture_href}

@view_config(route_name='view_picture', renderer='view_picture.mako')
def view_picture(request):
    username, album_name, picture_name = \
        request.matchdict['username'], \
        request.matchdict['album_name'], \
        request.matchdict['picture_name'],
    user = DBSession.query(UserModel).\
        filter(UserModel.name == username).\
        first()
    album = user.albums[album_name]
    picture = album.pictures[picture_name]
    #album = DBSession.query(AlbumModel).join(UserModel).\
    #    filter(AlbumModel.name == album_name).\
    #    filter(AlbumModel.user_id == UserModel.id).\
    #    filter(UserModel.name == username).\
    #    first()
    #picture = DBSession.query(PictureModel).\
    #    filter(PictureModel.name == picture_name).\
    #    filter(PictureModel.album_id == album.id).\
    #    first()

    return {'username' : username, 'album' : album, 'picture' : picture}    
