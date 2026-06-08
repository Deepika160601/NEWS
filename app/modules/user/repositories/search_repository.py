from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.models import News


# =========================
# SEARCH NEWS
# =========================
async def search_news(
    db: AsyncSession,
    keyword: str
):

    result = await db.execute(
        select(News)
        .where(
            News.title.ilike(
                f"%{keyword}%"
            ),
            News.status == "published"
        )
    )

    return result.scalars().all()