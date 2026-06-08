from fastapi import (
    APIRouter,
    Depends
)

from sqlalchemy.ext.asyncio import (
    AsyncSession
)

from app.db.db import get_db

from app.core.security import (
    get_current_user
)

from app.modules.user.services.notification_service import (
    get_user_notifications_service,
    get_unread_notifications_service,
    mark_notification_as_read_service
)

router = APIRouter()


# =========================
# GET MY NOTIFICATIONS
# =========================
@router.get("/")
async def get_notifications(
    db: AsyncSession = Depends(get_db),
    current_user=Depends(get_current_user)
):

    return await get_user_notifications_service(
        db,
        current_user["user_id"]
    )