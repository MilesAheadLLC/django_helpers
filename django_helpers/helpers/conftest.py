import pytest
from os import environ
from selenium import webdriver
from django.core import mail
from django.core.management import call_command

from django.conf import settings

browsers = {
    'firefox': webdriver.Firefox,
    }

@pytest.fixture(scope='session', params=browsers.keys())
def web_browser(request):
    '''
     Sets up and tears down browser instance
    '''
    if 'DISPLAY' not in environ:
        pytest.skip('Test requires display server (export DISPLAY)')

    browser = browsers[request.param]()
    # Wait a maximum of 3 seconds to ensure that page has loaded
    browser.implicitly_wait(3)

    request.addfinalizer(lambda *args: browser.quit())

    return browser


@pytest.fixture(scope='session')
def email_mem_backend(request):
    '''
        Sets up and tears down django local memory email backend

        Usage: In function you are testing messages are stored in list that is in mail.outbox after email is sent
    '''
    # Get local memory backend
    backend = mail.get_connection(backend='django.core.mail.backends.locmem.EmailBackend')
    backend.open()
    # Because not using django's TestCase we need to empty the mailbox
    if mail.outbox:
        mail.outbox = []

    request.addfinalizer(lambda *args: backend.close())

    return backend

@pytest.fixture(scope='session')
def south_migrate(request):
    '''
     Runs the South Migrations
    '''
    call_command('migrate')