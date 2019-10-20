from rest_framework import serializers
from .models import Essay, Album, Files


class EssaySerializer(serializers.ModelSerializer):
    author_name = serializers.ReadOnlyField(source='author.username')
    class Meta:
        model = Essay
        fields = (
            'pk', 'title', 'body', 'author_name'
        )

class AlbumSerializer(serializers.ModelSerializer):
    author_name = serializers.ReadOnlyField(source='author.username')
    image = serializers.ImageField(use_url=True)

    class Meta:
        model = Album
        fields = (
        'pk', 'author_name', 'image', 'desc'
        )

class FileSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')
    myfile = serializers.FileField(use_url=True)

    class Meta:
        model = Files
        fields = (
        'pk', 'author', 'myfile', 'desc'
        )