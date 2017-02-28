from django.conf.urls import url, include
from django.contrib import admin
from rest_framework_swagger.views import get_swagger_view

from channels.routes import router

urlpatterns = [
    url(r'^$', get_swagger_view(title='Api documentation')),
    url(r'^admin/', admin.site.urls),
    url(r'api/v1/', include(router.urls))
]
