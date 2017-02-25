from rest_framework import serializers
from rest_framework_recursive.fields import RecursiveField


from .models import Channel, Category


class ChannelSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Channel
        fields = ('name', 'url')


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    subcategories = serializers.ListSerializer(
        source='children',
        child=RecursiveField(),
        required=False
    )

    class Meta:
        model = Category
        fields = ('name', 'channel', 'url', 'subcategories')
