from django.core.urlresolvers import reverse
from django.test.client import Client

def get_response(view_name):
    '''
     Returns a response object that can be used to test if the correct template is used
    '''
    return Client().get(reverse(view_name))

