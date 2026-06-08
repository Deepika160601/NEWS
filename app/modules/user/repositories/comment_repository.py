from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.models import Comment


# =========================
# ADD COMMENT
# =========================
async def add_comment(
    db: AsyncSession,
    data,
    user_id: int
):

    comment = Comment(
        user_id=user_id,
        news_id=data.news_id,
        content=data.content,
        parent_comment_id=data.parent_comment_id
    )

    db.add(comment)

    await db.commit()

    await db.refresh(comment)

    return comment


# =========================
# GET COMMENTS BY NEWS
# =========================
async def get_comments_by_news(
    db: AsyncSession,
    news_id: int
):

    result = await db.execute(
        select(Comment).where(
            Comment.news_id == news_id
        )
    )

    return result.scalars().all()