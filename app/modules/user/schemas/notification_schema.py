from pydantic import BaseModel
from datetime import datetime


# =========================
# NOTIFICATION RESPONSE
# =========================
class NotificationResponse(
    BaseModel
):

    notification_id: int

    user_id: int

    news_id: int | None = None

    title: str

    message: str

    is_read: bool

    created_at: datetime

    class Config:
        from_attributes = True