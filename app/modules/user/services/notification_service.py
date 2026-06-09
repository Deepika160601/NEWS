from fastapi import (
    HTTPException,
    status
)

from sqlalchemy.ext.asyncio import (
    AsyncSession
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
# GET UNREAD NOTIFICATIONS
# =========================
async def get_unread_notifications_service(
    db: AsyncSession,
    user_id: int
):

    notifications = await get_unread_notifications(
        db,
        user_id
    )

    return success_response(
        "Unread notifications fetched successfully",
        notifications
    )


# =========================
# MARK AS READ
# =========================
async def mark_notification_as_read_service(
    db: AsyncSession,
    notification_id: int
):

    notification = await get_notification_by_id(
        db,
        notification_id
    )

    if not notification:

        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Notification not found"
        )

    updated_notification = await mark_as_read(
        db,
        notification
    )

    return success_response(
        "Notification marked as read",
        updated_notification
    )