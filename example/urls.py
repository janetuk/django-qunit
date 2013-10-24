from django.conf.urls import *

urlpatterns = patterns('',
    url('^qunit/', include('django_qunit.urls'))
)
