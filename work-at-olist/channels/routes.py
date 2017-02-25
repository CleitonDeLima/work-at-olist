from rest_framework import routers

from .views import ChannelViewSet, CategoryViewSet

router = routers.DefaultRouter()
router.register(r'channels', ChannelViewSet)
router.register(r'categories', CategoryViewSet)
