from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.models import News
from datetime import datetime

# =========================
# CREATE NEWS
# =========================
async def create_news(
    db: AsyncSession,
    data
):

    news = News(
        **data
    )

    db.add(news)

    await db.commit()

    await db.refresh(news)

    return news


# =========================
# GET NEWS BY TITLE
# =========================
async def get_news_by_title(
    db: AsyncSession,
    title: str
):

    result = await db.execute(
        select(News).where(
            News.title == title
        )
    )

    return result.scalar_one_or_none()


# =========================
# GET NEWS BY ID
# =========================
async def get_news_by_id(
    db: AsyncSession,
    news_id: int
):

    result = await db.execute(
        select(News).where(
            News.news_id == news_id
        )
    )

    return result.scalar_one_or_none()


# =========================
# GET ALL NEWS
# =========================
async def get_all_news(
    db: AsyncSession
):

    result = await db.execute(
        select(News)
    )

    return result.scalars().all()


# PUBLISH NEWS
# =========================
async def publish_news(
    db: AsyncSession,
    news: News
):

    news.status = "published"
    news.published_at = datetime.utcnow()

    await db.commit()

    await db.refresh(news)

    return news


# =========================
# DELETE NEWS
# =========================
async def delete_news(
    db: AsyncSession,
    news: News
):

    await db.delete(news)

    await db.commit()