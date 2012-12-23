from pyramid.config import Configurator
from sqlalchemy import engine_from_config
from horus import groupfinder
from hem.interfaces import IDBSession
from pyramid.authentication import AuthTktAuthenticationPolicy
from pyramid.authorization  import ACLAuthorizationPolicy

from .models import (
    DBSession,
    Base,
)

def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    authentication_policy = AuthTktAuthenticationPolicy('seekrit',
        callback=groupfinder)
    authorization_policy = ACLAuthorizationPolicy()
    config = Configurator(
        settings = settings
        , authentication_policy = authentication_policy
        , authorization_policy=authorization_policy
    )

    engine = engine_from_config(settings, 'sqlalchemy.')
    DBSession.configure(bind=engine)
    Base.metadata.bind = engine
    config.registry.registerUtility(DBSession, IDBSession)

    config.override_asset(
        to_override='hiero:templates/blog_index.mako',
        override_with='hhblog:templates/blog_index.mako'
    )
    config.override_asset(
        to_override='hiero:templates/entry_detail.mako',
        override_with='hhblog:templates/entry_detail.mako'
    )

    config.add_route('index',        'lkjalsdkj')

    config.add_static_view('static', 'static', cache_max_age=3600)
    config.scan()
    config.include('horus', route_prefix='auth')
    config.include('hiero')
    config.scan()
    return config.make_wsgi_app()

