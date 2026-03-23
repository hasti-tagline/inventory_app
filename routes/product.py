from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from inventory_app import schemas, crud, database

router = APIRouter(prefix="/products", tags=["Products"])

@router.post("/", response_model=schemas.ProductResponse)
def create_product(product: schemas.ProductCreate, db: Session = Depends(database.get_db)):
    return crud.create_product(db, product)

@router.get("/", response_model=list[schemas.ProductResponse])
def get_products(db: Session = Depends(database.get_db)):
    return crud.get_products(db)


#  JOIN endpoint (Product + Supplier)
@router.get("/with-supplier")
def get_products_with_supplier(db: Session = Depends(database.get_db)):
    products = crud.get_products_with_supplier(db)

    result = []
    for p in products:
        result.append({
            "product_id": p.id,
            "product_name": p.name,
            "quantity": p.quantity,
            "supplier_name": p.supplier.name if p.supplier else None
        })

    return result