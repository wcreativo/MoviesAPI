from typing import Optional

from pydantic import BaseModel, Field


class Movie(BaseModel):
    id: Optional[int] = None
    title: str = Field(max_length=20)
    overview: str | None = None
    year: str
    rating: int = Field(ge=1, le=10)
    category: str
