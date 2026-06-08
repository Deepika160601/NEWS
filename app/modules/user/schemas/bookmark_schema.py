from pydantic import BaseModel


# =========================
# ADD BOOKMARK
# =========================
class BookmarkCreateRequest(
    BaseModel
):

    news_id: int


# =========================
# BOOKMARK RESPONSE
# =========================
class BookmarkResponse(
    BaseModel
):

    message: str