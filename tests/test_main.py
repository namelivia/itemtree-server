import pytest
from mock import patch, Mock, call
from .test_base import (
    client,
    create_test_database,
    database_test_session,
)
from app.items.models import Item
from app.items.schemas import Item as ItemSchema
from freezegun import freeze_time


@freeze_time("2013-04-09")
class TestApp:
    def _insert_test_item(self, session, item: dict = {}):
        data = {
            "name": "Test item",
            "description": "This is a test item",
            "parent_id": 1,
            "destination_id": 1,
            "is_container": False,
        }
        data.update(item)
        db_item = Item(**data)
        session.add(db_item)
        session.commit()
        return db_item

    @patch("app.notifications.notifications.Notifications.send")
    def test_create_item(
        self,
        m_send_notification,
        client,
        database_test_session,
    ):
        response = client.post(
            "/items",
            json={
                "name": "New item",
                "description": "This is a new item",
                "parent_id": 1,
                "destination_id": 1,
                "is_container": False,
            },
        )
        assert response.status_code == 201
        assert response.json() == {
            "id": 1,
            "name": "New item",
            "description": "This is a new item",
            "parent_id": 1,
            "destination_id": 1,
            "is_container": False,
        }
        m_send_notification.assert_called_with("The item New item has been created")

    def test_get_non_existing_item(self, client):
        response = client.get("/items/99")
        assert response.status_code == 404

    @patch("app.users.api.UserInfo.get_current")
    def test_get_current_user(self, m_get_user_info, client):
        m_get_user_info.return_value = {
            "aud": ["example"],
            "email": "user@example.com",
            "exp": 1237658,
            "iat": 1237658,
            "iss": "test.example.com",
            "nbf": 1237658,
            "sub": "user",
            "name": "User Name",
        }
        response = client.get(
            "/users/me", headers={"X-Pomerium-Jwt-Assertion": "jwt_assertion"}
        )
        assert response.status_code == 200
        assert response.json() == {
            "aud": ["example"],
            "email": "user@example.com",
            "exp": 1237658,
            "iat": 1237658,
            "iss": "test.example.com",
            "nbf": 1237658,
            "sub": "user",
            "name": "User Name",
        }
        m_get_user_info.assert_called_with("jwt_assertion")

    def test_get_existing_item(self, client, database_test_session):
        self._insert_test_item(database_test_session)
        response = client.get("/items/1")
        assert response.status_code == 200
        assert response.json() == {
            "id": 1,
            "name": "Test item",
            "description": "This is a test item",
            "parent_id": 1,
            "destination_id": 1,
            "is_container": False,
        }

    def test_create_item_invalid(self, client):
        response = client.post("/items", json={"payload": "Invalid"})
        assert response.status_code == 422

    def test_get_all_items(self, client, database_test_session):
        self._insert_test_item(database_test_session)
        self._insert_test_item(database_test_session)
        response = client.get("/items")
        assert response.status_code == 200
        assert response.json() == [
            {
                "id": 1,
                "name": "Test item",
                "description": "This is a test item",
                "parent_id": 1,
                "destination_id": 1,
                "is_container": False,
            },
            {
                "id": 2,
                "name": "Test item",
                "description": "This is a test item",
                "parent_id": 1,
                "destination_id": 1,
                "is_container": False,
            },
        ]

    def test_delete_non_existing_item(self, client):
        response = client.get("/items/99")
        assert response.status_code == 404

    def test_delete_item(self, client, database_test_session):
        self._insert_test_item(database_test_session)
        response = client.get("/items/1")
        assert response.status_code == 200

    def test_updating_item(self, client, database_test_session):
        original_item = self._insert_test_item(
            database_test_session, {"name": "Some name"}
        )
        response = client.put(
            "/items/1",
            json={
                "name": "Updated item",
                "description": "This is a test item",
                "parent_id": 1,
                "destination_id": 1,
                "is_container": False,
            },
        )
        assert response.status_code == 200
        assert response.json() == {
            "id": 1,
            "name": "Updated item",
            "description": "This is a test item",
            "parent_id": 1,
            "destination_id": 1,
            "is_container": False,
        }
