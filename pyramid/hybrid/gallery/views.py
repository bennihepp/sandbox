from pyramid.view import view_config
from pyramid.httpexceptions import HTTPFound

#@view_config(route_name='home', renderer='templates/mytemplate.pt')
#def my_view(request):
#    return {'project':'gallery'}

def create_hybrid_url_factory(route_name, arguments=()):
    def hybrid_url(context, request, *elements, **kwargs):
        if 'query' in kwargs:
            kwargs['_query'] = kwargs['query']
            del kwargs['query']
        if 'anchor' in kwargs:
            kwargs['_anchor'] = kwargs['anchor']
            del kwargs['anchor']
        kwargs['traverse'] = traversal_path(model_path(context))
        for argument in arguments:
            kwargs[argument] = request.matchdict[argument]
        return request.route_url(route_name, *elements, **kwargs)
    return hybrid_url

hybrid_url = create_hybrid_url_factory('gallery', 'username')

def hybrid_view_config(*args, **kwargs):
    def hybrid_view_decorator(view_callable):
        def hybrid_view_callable(*inner_args):
            if len(inner_args) > 1:
                request = inner_args[1]
            else:
                request = inner_args[0]
            print 'monkey patched', str(len(inner_args))
            request.hybrid_url = hybrid_url
            print request
            print request.hybrid_url
            return view_callable(*inner_args)
        return view_config(*args, **kwargs)(hybrid_view_callable)
    return hybrid_view_decorator

@view_config(route_name='home')
def home_view(request):
    print 'home_view()'
    #print 'redirect to:', hybrid_url('gallery_default')
    #return HTTPFound(location=hybrid_url('gallery_default'))
    return HTTPFound(location=request.route_url('gallery_default', traverse=''))

@hybrid_view_config(route_name='gallery_default', renderer='templates/mytemplate.pt')
@hybrid_view_config(route_name='gallery', renderer='templates/mytemplate.pt')
def gallery_view(context, request):
    return {'project':'gallery'}
