from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from inventory_app import schemas, crud, database

router = APIRouter(prefix="/suppliers", tags=["Suppliers"])

@router.post("/", response_model=schemas.SupplierResponse)
def create_supplier(supplier: schemas.SupplierCreate, db: Session = Depends(database.get_db)):
    return crud.create_supplier(db, supplier)

@router.get("/", response_model=list[schemas.SupplierResponse])
def get_suppliers(db: Session = Depends(database.get_db)):
    return crud.get_suppliers(db)