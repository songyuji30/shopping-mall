from typing import Optional
from pydantic import BaseModel, HttpUrl

class ProductBase(BaseModel):
    # id: int
    # category_id: int
    name: str
    description: Optional[str] = None
    price: float
    image_url: Optional[HttpUrl] = None


class ProductCreate(ProductBase):
    category_id: int

class ProductUpdate(ProductBase):
    category_id: Optional[int] = None
    # name: Optional[str]
    # description: Optional[str]
    # price: Optional[float]
    # image_url: Optional[HttpUrl]
    
class ProductInDBBase(ProductBase):
    id: int
    category_id: int

    class Config:
        from_attributes = True

class ProductInDB(ProductInDBBase):
    pass

class Product(ProductInDBBase):
    pass