import pytest
from freezegun import freeze_time
from mixer.backend.django import mixer

from pages.models import Page


@pytest.fixture
def page():
    with freeze_time('1001-01-01 01:00'):
        return mixer.blend(Page)
