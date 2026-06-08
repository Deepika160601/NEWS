from fastapi import (
    HTTPException,
    status
)

from sqlalchemy.ext.asyncio import (
    AsyncSession
)

from app.modules.user.repositories.news_repository import (
    get_latest_news,
    get_news_by_id
)


# =========================
# GET LATEST NEWS
# =========================
async def get_latest_news_service(
    db: AsyncSession
):

    news = await get_latest_news(
        db
    )

    if not news:

        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="No news found"
        )

    return news


# =========================
# GET NEWS DETAILS
# =========================
async def get_news_by_id_service(
    db: AsyncSession,
    news_id: int
):

    news = await get_news_by_id(
        db,
        news_id
    )

    if not news:

        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="News not found"
        )

    return news