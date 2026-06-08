from pydantic import BaseModel
from typing import Optional


# =========================
# NEWS RESPONSE
# =========================
class NewsResponse(BaseModel):

    news_id: int

    title: str

    content: str

    summary: Optional[str]

    category_id: int

    location_id: int

    author_id: int

    is_breaking: bool

    thumbnail_url: Optional[str]

    view_count: int

    like_count: int

    comment_count: int

    class Config:
        from_attributes = True