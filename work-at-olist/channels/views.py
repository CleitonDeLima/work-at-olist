from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response

from .models import Channel, Category
from .serializers import ChannelSerializer, CategorySerializer, \
    ChannelCategoriesSerializer


class ChannelViewSet(viewsets.ReadOnlyModelViewSet):
    """
    list:
        Returns the list of all channels
    retrieve:
        Returns the information channel with its categories
    """
    serializer_class = ChannelSerializer
    queryset = Channel.objects.all()

    def retrieve(self, request, *args, **kwargs):
        channel = self.get_object()
        serializer = ChannelCategoriesSerializer(channel)
        return Response(serializer.data)


class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    """
    list:
        Returns the list of all categories and yours childrens
    retrieve:
        Returns the information category and your childrens
    """
    serializer_class = CategorySerializer
    queryset = Category.objects.root_nodes()

    def retrieve(self, request, *args, **kwargs):
        instance = get_object_or_404(Category, **kwargs)
        serializer = self.get_serializer(instance)
        return Response(serializer.data)
