from fastapi import (
    HTTPException,
    status
)

from sqlalchemy.ext.asyncio import (
    AsyncSession
)

from app.modules.user.repositories.bookmark_repository import (
    add_bookmark,
    get_user_bookmarks,
    remove_bookmark
)


# =========================
# ADD BOOKMARK
# =========================
async def add_bookmark_service(
    db: AsyncSession,
    user_id: int,
    news_id: int
):

    await add_bookmark(
        db,
        user_id,
        news_id
    )

    return {
        "message": "News bookmarked successfully"
    }


# =========================
# GET USER BOOKMARKS
# =========================
async def get_user_bookmarks_service(
    db: AsyncSession,
    user_id: int
):

    return await get_user_bookmarks(
        db,
        user_id
    )


# =========================
# REMOVE BOOKMARK
# =========================
async def remove_bookmark_service(
    db: AsyncSession,
    user_id: int,
    news_id: int
):

    bookmark = await remove_bookmark(
        db,
        user_id,
        news_id
    )

    if not bookmark:

        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Bookmark not found"
        )

    return {
        "message": "Bookmark removed successfully"
    }