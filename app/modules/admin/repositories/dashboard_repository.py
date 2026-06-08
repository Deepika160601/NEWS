from sqlalchemy import select, func
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.models import (
    User,
    News,
    Category,
    Poll
)


class DashboardRepository:

    @staticmethod
    async def get_dashboard_stats(
        db: AsyncSession
    ):

        total_users = await db.scalar(
            select(func.count(User.user_id))
        )

        total_news = await db.scalar(
            select(func.count(News.news_id))
        )

        published_news = await db.scalar(
            select(func.count(News.news_id))
            .where(
                News.status == "published"
            )
        )

        draft_news = await db.scalar(
            select(func.count(News.news_id))
            .where(
                News.status == "draft"
            )
        )

        total_categories = await db.scalar(
            select(func.count(Category.category_id))
        )

        total_polls = await db.scalar(
            select(func.count(Poll.poll_id))
        )

        return {
            "total_users": total_users or 0,
            "total_news": total_news or 0,
            "published_news": published_news or 0,
            "draft_news": draft_news or 0,
            "total_categories": total_categories or 0,
            "total_polls": total_polls or 0
        }