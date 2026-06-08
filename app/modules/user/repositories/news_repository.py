from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.models import News


# =========================
# GET LATEST NEWS
# =========================
async def get_latest_news(
    db: AsyncSession
):

    result = await db.execute(
        select(News)
        .where(
            News.status == "published"
        )
        .order_by(
            News.created_at.desc()
        )
    )

    return result.scalars().all()


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