import pytest
import requests as rq

STATUSES = {200: 'success',
            404: 'error'}


@pytest.fixture(params=['https://dog.ceo/api/breed'])
def fixture_url(request):
    return request.param


def test_dog_api_breads_all(fixture_url):
    """ Получение списка всех пород и подпород """
    url = f'{fixture_url}s/list/all'
    response = rq.get(url)
    assert response.status_code == 200
    assert response.json()['status'] == STATUSES[200]


def test_dog_api_random_image(fixture_url):
    """ Получение рандомного изображения, независимо от породы """
    url = f"{fixture_url}s/image/random"
    response = rq.get(url)
    assert response.status_code == 200
    assert response.json()["status"] == "success"


@pytest.mark.parametrize(
    ("breed", "status_code"),
    [
        pytest.param("hound", 200, id=' | Exists'),
        pytest.param("pug", 200, id=' | Exists'),
        pytest.param("miss name", 404, id=' | Not exists')
    ])
def test_dog_api_breeds_random(fixture_url, breed, status_code: int):
    """ Получение рандомного изображения по породе """
    url = f"{fixture_url}/{breed}/images/random"
    response = rq.get(url)
    assert response.status_code == status_code
    assert response.json()["status"] == STATUSES[status_code]


@pytest.mark.parametrize(
    ("breed", "subbreed", "status_code"),
    [
        pytest.param("hound", 'afghan', 200, id=' | Exists'),
        pytest.param("hound", 'english',  200, id=' | Exists'),
        pytest.param("HOUND", 'english',  404, id=' | Not exists cause caps'),
        pytest.param("miss name", 'mis sub', 404, id=' | Not exists')
    ])
def test_dog_api_breeds_random(fixture_url, breed, subbreed, status_code: int):
    """ Получение рандомного изображения по породе """
    url = f"{fixture_url}/{breed}/{subbreed}/images/random"
    response = rq.get(url)
    assert response.status_code == status_code
    assert response.json()["status"] == STATUSES[status_code]


@pytest.mark.parametrize(
    ("breed", 'amount', "status_code"),
    [
        pytest.param("akita", 4, 200, id=' | akita 4'),
        pytest.param("husky", 189, 200, id=' | husky 189'),
    ])
def test_dog_api_breeds_random_with_amount(fixture_url, breed, amount, status_code: int):
    """ Получение рандомного изображения по породе """
    url = f"{fixture_url}/{breed}/images/random/{amount}"
    response = rq.get(url)
    assert response.status_code == status_code
    assert response.json()["status"] == STATUSES[status_code]
    assert len(response.json()['message']) == amount


@pytest.mark.parametrize(
    ("breed", 'amount', "status_code"),
    [
        pytest.param("akita", -1, 200, id=' | akita -1'),
        pytest.param("husky", 0, 200, id=' | husky 0'),
        pytest.param("shiba", 2000, 200, id=' | shiba Not exists'),
    ])
def test_negative_dog_api_breeds_random_with_amount(
        fixture_url, breed, amount, status_code: int
):
    """ Получение рандомного изображения по породе """
    url = f"{fixture_url}/{breed}/images/random/{amount}"
    response = rq.get(url)
    assert response.status_code == status_code
    assert response.json()["status"] == STATUSES[status_code]
    assert len(response.json()['message']) != amount
