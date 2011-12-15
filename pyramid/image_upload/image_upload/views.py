import os

from pyramid.httpexceptions import (
    HTTPFound,
    HTTPNotFound,
    HTTPForbidden,
)
from pyramid.view import view_config

from .models import (
    DBSession,
    MyModel,
    )

@view_config(route_name='home')
def home(request):
    return HTTPFound(location = request.route_url('file_selector'))

@view_config(route_name='file_selector', renderer='file_selector.mako')
def file_selector(request):
    return {}
    #one = DBSession.query(MyModel).filter(MyModel.name=='one').first()
    #return {'one':one, 'project':'image_upload'}

@view_config(route_name='upload', renderer='json')
def upload(request):
	files = request.params['files']
	print dir(request.params)
	filename = os.path.basename(files.filename)
	print files.filename
	f = files.file
	# goto end of file
	f.seek(0, 2)
	size = f.tell()
	return [{"name":filename,"size":size,"url":"\/\/example.org\/files\/%s" % filename,"thumbnail_url":"\/\/example.org\/thumbnails\/%s" % filename,"delete_url":"\/\/example.org\/upload-handler?file=%s" % filename,"delete_type":"DELETE"}]
