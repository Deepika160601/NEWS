from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

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

    news_list = result.scalars().all()

    return [
        {
            "news_id": news.news_id,
            "title": news.title,
            "summary": news.summary,
            "thumbnail_url": news.thumbnail_url,
            "category_id": news.category_id,
            "is_breaking": news.is_breaking,
            "like_count": news.like_count,
            "comment_count": news.comment_count,
            "view_count": news.view_count,
            "published_at": news.published_at,
            "created_at": news.created_at
        }
        for news in news_list
    ]


# =========================
# GET NEWS BY ID
# =========================
async def get_news_by_id(
    db: AsyncSession,
    news_id: int
):

    result = await db.execute(
        select(News)
        .options(
            selectinload(News.location)
        )
        .where(
            News.news_id == news_id,
            News.status == "published"
        )
    )

    news = result.scalar_one_or_none()

    if not news:
        return None

    # Increment View Count
    news.view_count += 1

    await db.commit()

    await db.refresh(news)

    return {
        "news_id": news.news_id,
        "title": news.title,
        "content": news.content,
        "summary": news.summary,
        "thumbnail_url": news.thumbnail_url,
        "video_url": news.video_url,
        "category_id": news.category_id,
        "location": {
            "state": news.location.state if news.location else None,
            "district": news.location.district if news.location else None,
            "city": news.location.city if news.location else None
        },
        "is_breaking": news.is_breaking,
        "like_count": news.like_count,
        "comment_count": news.comment_count,
        "view_count": news.view_count,
        "published_at": news.published_at,
        "created_at": news.created_at
    }