from pydantic import BaseModel
from typing import Optional

#supplier
class SupplierCreate(BaseModel):
    name: str
    email: Optional[str] = None

class SupplierResponse(BaseModel):
    id: int
    name: str
    email: Optional[str]

    class Config:
        from_attributes = True


#Product
class ProductCreate(BaseModel):
    name: str
    quantity: int
    supplier_id: Optional[int]

class ProductResponse(BaseModel):
    id: int
    name: str
    quantity: int
    supplier_id: Optional[int]

    class Config:
        from_attributes = True