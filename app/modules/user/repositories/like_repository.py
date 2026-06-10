from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.models import (
    Like,
    News
)


# =========================
# LIKE NEWS
# =========================
async def like_news(
    db: AsyncSession,
    user_id: int,
    news_id: int
):

    result = await db.execute(
        select(Like).where(
            Like.user_id == user_id,
            Like.news_id == news_id
        )
    )

    existing = result.scalar_one_or_none()

    if existing:
        return "already_liked"

    like = Like(
        user_id=user_id,
        news_id=news_id
    )

    db.add(like)

    result = await db.execute(
        select(News).where(
            News.news_id == news_id
        )
    )

    news = result.scalar_one_or_none()

    if news:
        news.like_count += 1

    await db.commit()

    await db.refresh(like)

    return like


# =========================
# UNLIKE NEWS
# =========================
async def unlike_news(
    db: AsyncSession,
    user_id: int,
    news_id: int
):

    result = await db.execute(
        select(Like).where(
            Like.user_id == user_id,
            Like.news_id == news_id
        )
    )

    like = result.scalar_one_or_none()

    if not like:
        return None

    await db.delete(like)

    result = await db.execute(
        select(News).where(
            News.news_id == news_id
        )
    )

    news = result.scalar_one_or_none()

    if news and news.like_count > 0:
        news.like_count -= 1

    await db.commit()

    return like