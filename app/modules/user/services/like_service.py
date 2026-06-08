from fastapi import (
    HTTPException,
    status
)

from sqlalchemy.ext.asyncio import (
    AsyncSession
)

from sqlalchemy import select

from app.models.models import News

from app.modules.user.repositories.like_repository import (
    like_news,
    unlike_news
)


# =========================
# LIKE NEWS
# =========================
async def like_news_service(
    db: AsyncSession,
    user_id: int,
    news_id: int
):

    if user_id <= 0:

        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid user id"
        )

    if news_id <= 0:

        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid news id"
        )

    await like_news(
        db,
        user_id,
        news_id
    )

    result = await db.execute(
        select(News).where(
            News.news_id == news_id
        )
    )

    news = result.scalar_one_or_none()

    return {
        "message": "News liked successfully",
        "like_count": news.like_count
    }


# =========================
# UNLIKE NEWS
# =========================
async def unlike_news_service(
    db: AsyncSession,
    user_id: int,
    news_id: int
):

    like = await unlike_news(
        db,
        user_id,
        news_id
    )

    if not like:

        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Like not found"
        )

    result = await db.execute(
        select(News).where(
            News.news_id == news_id
        )
    )

    news = result.scalar_one_or_none()

    return {
        "message": "News unliked successfully",
        "like_count": news.like_count
    }