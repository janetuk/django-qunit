
from django.conf import settings

try:
    settings.QUNIT_TEST_DIRECTORY
except AttributeError:
    from django.core.exceptions import ImproperlyConfigured

    raise ImproperlyConfigured('Missing required setting QUNIT_TEST_DIRECTORY.')
