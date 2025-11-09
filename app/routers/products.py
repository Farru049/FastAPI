from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.models import Product
from app.database import get_db
from app.schemas import ProductBase
router = APIRouter(
    prefix = "/products",
    tags = ["Products"] 
)

@router.post("/", response_model = ProductBase, status_code = 201)
def create_product(product:ProductBase, db:Session = Depends(get_db)):
    db_product = Product(name = product.name, price = product.price, description = product.description)
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product