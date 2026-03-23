from sqlalchemy.orm import Session
from inventory_app import models, schemas

# Supplier
def create_supplier(db: Session, supplier: schemas.SupplierCreate):
    db_supplier = models.Supplier(
        name=supplier.name,
        email=supplier.email
    )
    db.add(db_supplier)
    db.commit()
    db.refresh(db_supplier)
    return db_supplier

def get_suppliers(db: Session):
    return db.query(models.Supplier).all()


#Product
def create_product(db: Session, product: schemas.ProductCreate):
    db_product = models.Product(
        name=product.name,
        quantity=product.quantity,
        supplier_id=product.supplier_id
    )
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product

def get_products(db: Session):
    return db.query(models.Product).all()


#JOIN Example 
def get_products_with_supplier(db: Session):
    return db.query(models.Product).join(models.Supplier).all()