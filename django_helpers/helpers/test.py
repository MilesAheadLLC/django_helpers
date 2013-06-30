from django.core.urlresolvers import reverse
from django.contrib.sites.models import Site
from urlparse import urlparse
from django_webtest import WebTest

def get_response(view_name, client):
    '''
     Returns a response object for a named view uses Django's Test Client either through Django TestCase
     or client fixture from pytest_django
    '''
    return client.get(reverse(view_name))

def get_status_code(view_name, client):
    '''
     Convenience function to return just the status code of the response object from get_response
    '''
    return get_response(view_name, client).status_code

def reset_domain(live_server_url):
    """
     Resets site domain to that of the live server
    """
    current_site = Site.objects.get_current()
    url = urlparse(live_server_url)
    current_site.domain = url.netloc

class WebTestHelpers(WebTest):
    """
     Provides helpers for django webtest based tests
    """
    def get_status_code(self, view_name):
        """
         Returns status code for a django view using WebTest instead of Django's client
        """
        res = self.app.get(reverse(view_name))
        return res.status_code

    def get_response(self, view_name):
        """
         Returns the response to a view and follows the views redirect
        """
        res = self.app.get(reverse(view_name))
        return res
