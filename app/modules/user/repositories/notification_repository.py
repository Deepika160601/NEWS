from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.models import Notification


# =========================
# CREATE NOTIFICATION
# =========================
async def create_notification(
    db: AsyncSession,
    user_id: int,
    news_id: int,
    title: str,
    message: str
):

    notification = Notification(
        user_id=user_id,
        news_id=news_id,
        title=title,
        message=message,
        type="news",
        target_type="all"
    )

    db.add(notification)

    await db.commit()

    await db.refresh(notification)

    return notification


# =========================
# GET USER NOTIFICATIONS
# =========================
async def get_user_notifications(
    db: AsyncSession,
    user_id: int
):

    result = await db.execute(
        select(Notification)
        .where(
            Notification.user_id == user_id
        )
        .order_by(
            Notification.created_at.desc()
        )
    )

    return result.scalars().all()


# =========================
# GET NOTIFICATION BY ID
# =========================
async def get_notification_by_id(
    db: AsyncSession,
    notification_id: int
):

    result = await db.execute(
        select(Notification).where(
            Notification.notification_id == notification_id
        )
    )

    return result.scalar_one_or_none()


# =========================
# MARK AS READ
# =========================
async def mark_as_read(
    db: AsyncSession,
    notification: Notification
):

    notification.is_read = True

    await db.commit()

    await db.refresh(notification)

    return notification


# =========================
# GET UNREAD NOTIFICATIONS
# =========================
async def get_unread_notifications(
    db: AsyncSession,
    user_id: int
):

    result = await db.execute(
        select(Notification)
        .where(
            Notification.user_id == user_id,
            Notification.is_read == False
        )
    )

    return result.scalars().all()