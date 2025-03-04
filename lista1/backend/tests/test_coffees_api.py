# coding: utf-8

from fastapi.testclient import TestClient


from pydantic import StrictInt  # noqa: F401
from typing import Any, List  # noqa: F401
from openapi_server.models.coffee import Coffee  # noqa: F401


def test_add_coffee(client: TestClient):
    """Test case for add_coffee

    Add a new coffee drink
    """
    coffee = {"price":2.5,"name":"Espresso","description":"A strong and rich coffee drink","id":1}

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "POST",
    #    "/coffees",
    #    headers=headers,
    #    json=coffee,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_delete_coffee(client: TestClient):
    """Test case for delete_coffee

    Delete a coffee drink
    """

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "DELETE",
    #    "/coffees/{coffee_id}".format(coffee_id=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_get_coffee_by_id(client: TestClient):
    """Test case for get_coffee_by_id

    Get details of a specific coffee drink
    """

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/coffees/{coffee_id}".format(coffee_id=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_get_coffees(client: TestClient):
    """Test case for get_coffees

    Get a list of all coffee drinks
    """

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/coffees",
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_update_coffee(client: TestClient):
    """Test case for update_coffee

    Update a coffee drink
    """
    coffee = {"price":2.5,"name":"Espresso","description":"A strong and rich coffee drink","id":1}

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "PUT",
    #    "/coffees/{coffee_id}".format(coffee_id=56),
    #    headers=headers,
    #    json=coffee,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

