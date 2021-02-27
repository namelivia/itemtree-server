from pydantic import BaseModel, Field
from typing import Optional


class ItemBase(BaseModel):
    name: str = Field(title="Name for the item")
    description: str = Field(title="Name for the item")
    parent_id: Optional[int] = Field(title="Parent id for the item")
    destination_id: Optional[int] = Field(title="Parent id for the item")
    is_container: bool = Field(title="Indicates if the item is container or not")
    image: Optional[str] = Field(title="Image url for the item")


class ItemCreate(ItemBase):
    pass


class ItemUpdate(ItemBase):
    pass


class Item(ItemBase):
    id: int

    class Config:
        orm_mode = True
