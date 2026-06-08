from pydantic import BaseModel


# =========================
# LIKE REQUEST
# =========================
class LikeRequest(BaseModel):

    news_id: int