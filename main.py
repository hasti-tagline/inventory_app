from fastapi import FastAPI
from inventory_app.database import Base, engine
from inventory_app.routes import product, supplier

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Inventory Management API")

#main app
app.include_router(product.router)
app.include_router(supplier.router)

@app.get("/jobs/count")
def get_job_count():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM jobs")
    count = cursor.fetchone()[0]
    cursor.close()
    conn.close()
    return {"total_jobs": count}