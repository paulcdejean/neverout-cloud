from django.conf.urls import include, url

from django.contrib import admin
admin.autodiscover()

import backend.views

urlpatterns = [
    url(r'^add_point/([-+]?[0-9]*\.?[0-9]+)$', backend.views.add_point, name='add_point'),
    url(r'^admin/', include(admin.site.urls)),
]
