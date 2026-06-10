from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

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
        select(Comment)
        .options(selectinload(Comment.user))
        .where(
            Comment.news_id == news_id
        )
        .order_by(
            Comment.created_at.desc()
        )
    )

    comments = result.scalars().all()

    return [
        {
            "comment_id": comment.comment_id,
            "user_id": comment.user_id,
            "user_name": comment.user.name if comment.user else None,
            "news_id": comment.news_id,
            "content": comment.content,
            "parent_comment_id": comment.parent_comment_id,
            "created_at": comment.created_at
        }
        for comment in comments
    ]