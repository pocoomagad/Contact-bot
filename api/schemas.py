from pydantic import BaseModel

from typing import Generic, TypeVar

from pydantic.generics import GenericModel

T = TypeVar("T")

class Page(GenericModel, Generic[T]):
    """Model to represent a page of results along with pagination metadata."""

    items: list[T] = Field(ge=0, description="List of items on this Page")
    page_size: int = Field(ge=1, description="Number of items in this page")
    page: int = Field(ge=1, description="Current page number")