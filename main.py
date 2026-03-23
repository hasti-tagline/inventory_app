from fastapi import FastAPI
from inventory_app.database import Base, engine
from inventory_app.routes import product, supplier

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Inventory Management API")

#main app
app.include_router(product.router)
app.include_router(supplier.router)