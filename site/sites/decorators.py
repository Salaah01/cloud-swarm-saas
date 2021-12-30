from functools import wraps
from django import http
from django.contrib.auth.decorators import login_required
from . import models as site_models


def required_site_access(func):
    """Decorator to check if user has access to a site."""
    @wraps(func)
    @login_required
    def wrapper(
        request: http.HttpRequest,
        id: int,
        slug: str,
        *args,
        **kwargs
    ) -> http.HttpResponse:
        """Wrapper function.
        Args:
            request (HttpRequest): The request object.
            id (int): The site ID.
            slug (str): The site slug.
        """
        site = site_models.Site.for_id_slug(id, slug)
        if site is None:
            return http.HttpResponseNotFound()
        site_access = site_models.SiteAccess.user_access(site, request.user)
        if site_access is None:
            return http.HttpResponseNotFound()
        return func(request, site, site_access, *args, **kwargs)
    return wrapper