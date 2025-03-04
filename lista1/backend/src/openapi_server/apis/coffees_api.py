# coding: utf-8

from typing import Dict, List  # noqa: F401
import importlib
import pkgutil

from openapi_server.apis.coffees_api_base import BaseCoffeesApi
import openapi_server.impl
from openapi_server.models.coffee import Coffee

from fastapi import (  # noqa: F401
    APIRouter,
    Body,
    Cookie,
    Depends,
    Form,
    Header,
    HTTPException,
    Path,
    Query,
    Response,
    Security,
    status,
)

from openapi_server.models.extra_models import TokenModel  # noqa: F401
from pydantic import StrictInt
from typing import Any, List
from openapi_server.models.coffee import Coffee

# Lista przechowująca kawy
coffees_db = {}

router = APIRouter()

ns_pkg = openapi_server.impl
for _, name, _ in pkgutil.iter_modules(ns_pkg.__path__, ns_pkg.__name__ + "."):
    importlib.import_module(name)


# Subklasa CoffeesApi, implementujaca metody
class CoffeesApi(BaseCoffeesApi):
    # Metoda do dodawania kawy
    async def add_coffee(self, coffee: Coffee) -> Coffee:  # -> Zwraca coffee
        coffees_db[coffee.id] = coffee;  # id pobiera sie z src/open api server/models
        return coffee

        # Metoda do usuwania kawy

    async def delete_coffee(self, coffee_id: StrictInt):
        if coffee_id not in coffees_db:
            raise HTTPException(status_code=404, detail="Coffee not found")

        del coffees_db[coffee_id]
        return None

    # Metoda do wyswietlania informacji o konkretnej kawie
    async def get_coffee_by_id(self, coffee_id: StrictInt):
        if coffee_id not in coffees_db:
            raise HTTPException(status_code=404, detail="Coffee not found")

        return coffees_db[coffee_id]

    # Metoda do wyswietlania wszystkich kaw
    async def get_coffees(self):
        if not coffees_db:
            raise HTTPException(status_code=404, detail="No coffees found")

        return list(coffees_db.values())

    # Metoda do updatetowania kawy
    async def update_coffee(self, coffee_id: StrictInt, coffee: Coffee) -> Coffee:
        if coffee_id not in coffees_db:
            raise HTTPException(status_code=404, detail="Coffee not found")

        # Pobieranie kawy z db
        existing_coffee = coffees_db[coffee_id]

        # Aktualizujemy pola kawy
        if coffee.name:
            existing_coffee.name = coffee.name
        if coffee.description:
            existing_coffee.description = coffee.description
        if coffee.price:
            existing_coffee.price = coffee.price

        coffees_db[coffee_id] = existing_coffee

        return existing_coffee


@router.post(
    "/coffees",
    responses={
        201: {"description": "Coffee drink added successfully"},
    },
    tags=["Coffees"],
    summary="Add a new coffee drink",
    response_model_by_alias=True,
)
async def add_coffee(coffee: Coffee = Body(None, description=""), ) -> None:
    if not BaseCoffeesApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseCoffeesApi.subclasses[0]().add_coffee(coffee)


@router.delete(
    "/coffees/{coffee_id}",
    responses={
        204: {"description": "Coffee deleted successfully"},
        404: {"description": "Coffee not found"},
    },
    tags=["Coffees"],
    summary="Delete a coffee drink",
    response_model_by_alias=True,
)
async def delete_coffee(
        coffee_id: StrictInt = Path(..., description=""),
) -> None:
    if not BaseCoffeesApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseCoffeesApi.subclasses[0]().delete_coffee(coffee_id)


@router.get(
    "/coffees/{coffee_id}",
    responses={
        200: {"model": Coffee, "description": "Details of the coffee drink"},
        404: {"description": "Coffee not found"},
    },
    tags=["Coffees"],
    summary="Get details of a specific coffee drink",
    response_model_by_alias=True,
)
async def get_coffee_by_id(
        coffee_id: StrictInt = Path(..., description=""),
) -> Coffee:
    if not BaseCoffeesApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseCoffeesApi.subclasses[0]().get_coffee_by_id(coffee_id)


@router.get(
    "/coffees",
    responses={
        200: {"model": List[Coffee], "description": "A list of coffee drinks"},
    },
    tags=["Coffees"],
    summary="Get a list of all coffee drinks",
    response_model_by_alias=True,
)
async def get_coffees(
) -> List[Coffee]:
    if not BaseCoffeesApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseCoffeesApi.subclasses[0]().get_coffees()


@router.put(
    "/coffees/{coffee_id}",
    responses={
        200: {"description": "Coffee drink updated successfully"},
        404: {"description": "Coffee not found"},
    },
    tags=["Coffees"],
    summary="Update a coffee drink",
    response_model_by_alias=True,
)
async def update_coffee(
        coffee_id: StrictInt = Path(..., description=""),
        coffee: Coffee = Body(None, description=""),
) -> None:
    if not BaseCoffeesApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseCoffeesApi.subclasses[0]().update_coffee(coffee_id, coffee)