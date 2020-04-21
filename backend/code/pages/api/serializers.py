from rest_framework import serializers

from pages.models import Page


class PageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Page
        fields = [
            'id',
            'title',
            'content',
            'published_at',
            'created_at',
            'updated_at',
        ]
