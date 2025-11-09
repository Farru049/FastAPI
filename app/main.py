from fastapi import FastAPI
from app import models
from app.database import engine
from app.routers import welcome, products, reviews  # include your routers

# ✅ Create all database tables after models are imported
models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="My FastAPI App")

# ✅ Register routers
app.include_router(welcome.router)
app.include_router(products.router)
app.include_router(reviews.router)


