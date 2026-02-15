from pydantic import BaseModel, Field
from typing import Optional

class ItemBase(BaseModel):
    name: str = Field(..., min_length=2, max_length=100, example="Wiertarka")
    description: Optional[str] = Field(None, max_length=500)
    quantity: int = Field(ge=0, example=10)
    price: float = Field(gt=0, example=299.99)


class ItemCreate(ItemBase):
    pass


class ItemResponse(ItemBase):
    id: int

    class Config:
        from_attributes = True


class ItemUpdate(BaseModel):
    name: Optional[str] = Field(None, min_length=2, max_length=100)
    description: Optional[str] = None
    quantity: Optional[int] = Field(None, ge=0)
    price: Optional[float] = Field(None, gt=0)