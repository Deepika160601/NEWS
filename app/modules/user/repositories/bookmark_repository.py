from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.models import Bookmark


# =========================
# ADD BOOKMARK
# =========================
async def add_bookmark(
    db: AsyncSession,
    user_id: int,
    news_id: int
):

    result = await db.execute(
        select(Bookmark).where(
            Bookmark.user_id == user_id,
            Bookmark.news_id == news_id
        )
    )

    existing = result.scalar_one_or_none()

    if existing:
        return existing

    bookmark = Bookmark(
        user_id=user_id,
        news_id=news_id
    )

    db.add(bookmark)

    await db.commit()

    await db.refresh(bookmark)

    return bookmark


# =========================
# GET USER BOOKMARKS
# =========================
async def get_user_bookmarks(
    db: AsyncSession,
    user_id: int
):

    result = await db.execute(
        select(Bookmark).where(
            Bookmark.user_id == user_id
        )
    )

    return result.scalars().all()


# =========================
# REMOVE BOOKMARK
# =========================
async def remove_bookmark(
    db: AsyncSession,
    user_id: int,
    news_id: int
):

    result = await db.execute(
        select(Bookmark).where(
            Bookmark.user_id == user_id,
            Bookmark.news_id == news_id
        )
    )

    bookmark = result.scalar_one_or_none()

    if not bookmark:
        return None

    await db.delete(bookmark)

    await db.commit()

    return bookmark