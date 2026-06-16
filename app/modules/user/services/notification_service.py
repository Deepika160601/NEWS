from fastapi import (
    HTTPException,
    status
)

from sqlalchemy.ext.asyncio import (
    AsyncSession
)
from app.modules.user.repositories.user_repository import (
    UserRepository
)

from app.utils.api_response import success_response

from app.modules.user.repositories.notification_repository import (
    get_user_notifications,
    get_notification_by_id,
    mark_as_read,
    get_unread_notifications
)


# =========================
# GET USER NOTIFICATIONS
# =========================
async def get_user_notifications_service(
    db: AsyncSession,
    user_id: int
):

    notifications = await get_user_notifications(
        db,
        user_id
    )

    return success_response(
        "Notifications fetched successfully",
        notifications
    )
# =========================
# UPDATE NOTIFICATION SETTINGS
# =========================
async def update_notification_settings_service(
    db: AsyncSession,
    user_id: int,
    notification_enabled: bool
):

    user = await UserRepository.update_notification_settings(
        db,
        user_id,
        notification_enabled
    )

    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )

    return success_response(
        "Notification settings updated successfully",
        {
            "notification_enabled": user.notification_enabled
        }
    )


