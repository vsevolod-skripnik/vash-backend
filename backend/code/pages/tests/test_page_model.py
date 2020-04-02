import pytest
from django.utils import timezone
from freezegun import freeze_time

from pages.models import Page

pytestmark = [pytest.mark.django_db]


@pytest.mark.parametrize(
    'attribute',
    [
        'title',
        'content',
        'created_at',
        'updated_at',
        'published_at',
    ]
)
def test_attributes(page, attribute):
    assert hasattr(page, attribute)


@freeze_time('1001-01-01 01:00')
def test_created_at_auto_now_add(page):
    assert page.created_at == timezone.now()


@freeze_time('2002-02-02 02:00')
def test_updated_at_auto_now(page):
    page.update(title='The Ministry of Silly Walks')

    assert page.updated_at == timezone.now()


def test_published_at_none_by_default(page):
    assert page.published_at is None
