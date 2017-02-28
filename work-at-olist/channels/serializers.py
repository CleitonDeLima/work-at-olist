from rest_framework import serializers
from rest_framework_recursive.fields import RecursiveField


from .models import Channel, Category


class BaseCategorySerialzer(serializers.ModelSerializer):
    subcategories = serializers.ListSerializer(
        source='children',
        child=RecursiveField(),
        required=False
    )

    class Meta:
        model = Category
        fields = ('name', 'channel', 'subcategories')


class CategorySerializer(BaseCategorySerialzer, serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = ('name', 'channel', 'url', 'subcategories')


class ChannelSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Channel
        fields = ('name', 'url')


class ChannelCategoriesSerializer(serializers.ModelSerializer):
    categories_tree = serializers.ReadOnlyField(source='categories_recursive')

    class Meta:
        model = Channel
        fields = ('name', 'categories_tree')
