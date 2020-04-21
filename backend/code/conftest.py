import pytest
from freezegun import freeze_time
from mixer.backend.django import mixer

from pages.models import Page
from vash.utils.user_api_client import UserApiClient


@pytest.fixture
def anon():
    """Anonymous API Client"""
    return UserApiClient()


@pytest.fixture
def vash(anon, user):
    """Authenticated API Client"""
    anon.force_authenticate(user=user)
    return anon


@pytest.fixture
def page():
    with freeze_time('1001-01-01 01:00'):
        return mixer.blend(Page)
