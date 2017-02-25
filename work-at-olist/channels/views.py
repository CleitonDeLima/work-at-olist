from rest_framework import viewsets
from rest_framework.response import Response

from .models import Channel, Category
from .serializers import ChannelSerializer, CategorySerializer


class ChannelViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = ChannelSerializer
    queryset = Channel.objects.all()


class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.root_nodes()

    def retrieve(self, request, *args, **kwargs):
        instance = Category.objects.get(**kwargs)
        serializer = self.get_serializer(instance)
        return Response(serializer.data)
