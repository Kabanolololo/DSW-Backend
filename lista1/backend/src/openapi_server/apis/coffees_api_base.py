# coding: utf-8

from typing import ClassVar, Dict, List, Tuple  # noqa: F401

from pydantic import StrictInt
from typing import Any, List
from openapi_server.models.coffee import Coffee


class BaseCoffeesApi:
    subclasses: ClassVar[Tuple] = ()

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        BaseCoffeesApi.subclasses = BaseCoffeesApi.subclasses + (cls,)
    async def add_coffee(
        self,
        coffee: Coffee,
    ) -> None:
        ...


    async def delete_coffee(
        self,
        coffee_id: StrictInt,
    ) -> None:
        ...


    async def get_coffee_by_id(
        self,
        coffee_id: StrictInt,
    ) -> Coffee:
        ...


    async def get_coffees(
        self,
    ) -> List[Coffee]:
        ...


    async def update_coffee(
        self,
        coffee_id: StrictInt,
        coffee: Coffee,
    ) -> None:
        ...
