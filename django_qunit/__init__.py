
from bos2.config.common_settings import QUNIT_TEST_DIRECTORY


try:
    QUNIT_TEST_DIRECTORY
except AttributeError:
    from django.core.exceptions import ImproperlyConfigured

    raise ImproperlyConfigured('Missing required setting QUNIT_TEST_DIRECTORY.')
