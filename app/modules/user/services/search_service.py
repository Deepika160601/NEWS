from fastapi import (
    HTTPException,
    status
)

from sqlalchemy.ext.asyncio import (
    AsyncSession
)

from app.modules.user.repositories.search_repository import (
    search_news
)


# =========================
# SEARCH NEWS
# =========================
async def search_news_service(
    db: AsyncSession,
    keyword: str
):

    if not keyword.strip():

        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Keyword is required"
        )

    news = await search_news(
        db,
        keyword
    )

    if not news:

        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="No news found"
        )

    return news