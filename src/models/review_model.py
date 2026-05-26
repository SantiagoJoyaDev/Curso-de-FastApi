import datetime
from pydantic import BaseModel, Field

class Review(BaseModel):
    id: int
    user_id: int
    rating: int = Field(ge=0, le=10)
    review: str = Field(min_length=10, max_length=500)
    date: datetime.date

class CreateReview(BaseModel):
    user_id: int
    rating: int = Field(ge=0, le=10, default=0)
    review: str = Field(min_length=10, max_length=500, default="")
    date: datetime.date = Field(default=datetime.date.today())

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "user_id": 1,
                    "rating": 10,
                    "review": "Muy buena película",
                    "date": "2024-12-31",
                }
            ]
        }
    }

class UpdateReview(BaseModel):
    user_id: int = Field(default=0)
    rating: int = Field(default=0, ge=0, le=10)
    review: str = Field(default="", min_length=10, max_length=500)
    date: datetime.date = Field(default=datetime.date.today())