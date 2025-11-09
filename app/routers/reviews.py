from fastapi import APIRouter, HTTPException, status, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.models import Review
from app.schemas import ReviewsBase

router = APIRouter(
    prefix = "/reviews",
    tags = ["Reviews"]
)
@router.post("/", response_model=ReviewsBase)
async def create_review(review: ReviewsBase, db: Session = Depends(get_db)):
    db_review = Review(content = review.content, rating = review.rating)
    db.add(db_review)
    db.commit()
    db.refresh(db_review)