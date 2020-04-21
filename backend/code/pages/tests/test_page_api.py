import pytest

pytestmark = [pytest.mark.django_db]


def test_list_pages(anon, page):
    response = anon.get('/api/pages/')

    assert response.status_code == 200
    assert response.json()[0]['id'] == page.id


def test_retrieve_page(anon, page):
    response = anon.get(f'/api/pages/{page.id}/')

    assert response.status_code == 200
    assert response.json()['id'] == page.id

