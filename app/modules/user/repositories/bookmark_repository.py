from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.models import (
    Bookmark,
    News
)


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
        return "already_bookmarked"

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
        select(
            Bookmark.bookmark_id,
            Bookmark.news_id,
            Bookmark.created_at,
            News.title,
            News.summary,
            News.thumbnail_url
        )
        .join(
            News,
            Bookmark.news_id == News.news_id
        )
        .where(
            Bookmark.user_id == user_id
        )
    )

    rows = result.all()

    return [
        {
            "bookmark_id": row.bookmark_id,
            "news_id": row.news_id,
            "title": row.title,
            "summary": row.summary,
            "thumbnail_url": row.thumbnail_url,
            "created_at": row.created_at
        }
        for row in rows
    ]


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