from pyramid.view import view_config
from pyramid.httpexceptions import HTTPFound

#@view_config(route_name='home', renderer='templates/mytemplate.pt')
#def my_view(request):
#    return {'project':'gallery'}

@view_config(route_name='home')
def home_view(request):
    HTTPFound(location=request.route_url('gallery_default'))

@view_config(route_name='gallery', renderer='templates/mytemplate.pt')
def gallery_view(context, request):
    return {'project':'gallery'}
