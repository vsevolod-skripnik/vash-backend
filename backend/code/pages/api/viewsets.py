from rest_framework import mixins, viewsets

from pages.api.serializers import PageSerializer
from pages.models import Page


class PageViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    serializer_class = PageSerializer
    queryset = Page.objects.all()
