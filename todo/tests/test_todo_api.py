import pytest
from django.urls import reverse
from rest_framework.test import APIClient
from django.contrib.auth.models import User


@pytest.fixture
def api_client():
    client = APIClient()
    return client


@pytest.fixture
def commen_user():
    user = User.objects.create_user(username="test", password="Aa123456*")
    return user


@pytest.mark.django_db
class TestApiTask:
    def test_post_get_response_403_status(self, api_client):
        url = reverse("todo:api-v1:task-list")
        respone = api_client.get(url)

        assert respone.status_code == 403

    def test_post_get_response_200_status(self, api_client, commen_user):
        url = reverse("todo:api-v1:task-list")
        user = commen_user
        api_client.force_login(user=user)
        respone = api_client.get(url)

        assert respone.status_code == 200

    def test_post_create_response_200_status(self, api_client, commen_user):
        url = reverse("todo:api-v1:task-list")
        user = commen_user
        data = {
            "title": "test",
        }
        api_client.force_login(user=user)
        respone = api_client.post(url, data)

        assert respone.status_code == 201

    def test_post_create_response_invalid_data(self, api_client, commen_user):
        url = reverse("todo:api-v1:task-list")
        user = commen_user
        data = {}
        api_client.force_login(user=user)
        respone = api_client.post(url, data)

        assert respone.status_code == 400

    def test_post_detail_get_response_403_status(self, api_client):
        url = reverse("todo:api-v1:task-detail", kwargs={"pk": 1})
        respone = api_client.get(url)

        assert respone.status_code == 403
