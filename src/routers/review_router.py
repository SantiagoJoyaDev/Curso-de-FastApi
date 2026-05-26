from typing import List
from fastapi import Query, APIRouter
from src.models.review_model import Review, CreateReview, UpdateReview

reviews: List[Review] = []
review_router = APIRouter()


@review_router.post("/", tags=["Reviews"])
def create_review(review: CreateReview):
    reviews.append(review.model_dump())
    return review

@review_router.get("/", tags=["Reviews"])
def get_reviews_by_rating(rating: int = Query(default=None, ge=0, le=10)):
    results = [review for review in reviews if review["rating"] == rating]
    return results if results else {"message": "No se encontraron coincidencias"}

@review_router.put("/{id}", tags=["Reviews"])
def update_review(id: int, review: UpdateReview):
    for item in reviews:
        if item["id"] == id:
            item["user_id"] = review.user_id
            item["rating"] = review.rating
            item["review"] = review.review
            item["date"] = review.date
            return {
                "message": "Reseña actualizada con éxito",
                "current_reviews": reviews,
            }
    return {"message": "Reseña no encontrada"}

@review_router.delete("/{id}", tags=["Reviews"])
def delete_review(id: int):
    for review in reviews:
        if review["id"] == id:
            reviews.remove(review)
            return {"message": "Reseña eliminada con éxito", "current_reviews": reviews}
    return {"message": "Reseña no encontrada"}
