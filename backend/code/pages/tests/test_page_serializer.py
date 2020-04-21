import pytest

from pages.api.serializers import PageSerializer

pytestmark = [pytest.mark.django_db]


def test_serialize_page(page):
    serializer = PageSerializer(page)
    serializer.data  # No errors

