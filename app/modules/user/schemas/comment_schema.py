from pydantic import BaseModel
from typing import Optional


# =========================
# CREATE COMMENT
# =========================
class CommentCreateRequest(
    BaseModel
):

    news_id: int

    content: str

    parent_comment_id: Optional[int] = None


# =========================
# COMMENT RESPONSE
# =========================
class CommentResponse(
    BaseModel
):

    comment_id: int

    user_id: int

    news_id: int

    content: str

    parent_comment_id: Optional[int]

    class Config:
        from_attributes = True