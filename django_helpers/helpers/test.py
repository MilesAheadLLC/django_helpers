from django.core.urlresolvers import reverse

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
