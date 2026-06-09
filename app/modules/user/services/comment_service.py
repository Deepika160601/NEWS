from fastapi import (
    HTTPException,
    status
)

from sqlalchemy.ext.asyncio import (
    AsyncSession
)

from app.utils.api_response import success_response

from app.modules.user.repositories.comment_repository import (
    add_comment,
    get_comments_by_news
)


# =========================
# ADD COMMENT
# =========================
async def add_comment_service(
    db: AsyncSession,
    data,
    user_id: int
):

    if not data.content.strip():

        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Comment cannot be empty"
        )

    comment = await add_comment(
        db,
        data,
        user_id
    )

    return success_response(
        "Comment added successfully",
        comment
    )


# =========================
# GET COMMENTS
# =========================
async def get_comments_service(
    db: AsyncSession,
    news_id: int
):

    comments = await get_comments_by_news(
        db,
        news_id
    )

    if not comments:

        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="No comments found"
        )

    return success_response(
        "Comments fetched successfully",
        comments
    )