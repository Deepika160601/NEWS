from fastapi import (
    HTTPException,
    status
)

from sqlalchemy.ext.asyncio import (
    AsyncSession
)

from app.utils.api_response import success_response

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

    bookmark = await add_bookmark(
        db,
        user_id,
        news_id
    )

    if bookmark == "already_bookmarked":
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="News already bookmarked"
        )

    return success_response(
        "News bookmarked successfully",
        {
            "bookmark_id": bookmark.bookmark_id,
            "news_id": bookmark.news_id
        }
    )


# =========================
# GET USER BOOKMARKS
# =========================
async def get_user_bookmarks_service(
    db: AsyncSession,
    user_id: int
):

    bookmarks = await get_user_bookmarks(
        db,
        user_id
    )

    return success_response(
        "Bookmarks fetched successfully",
        bookmarks
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

    return success_response(
        "Bookmark removed successfully",
        {
            "news_id": news_id
        }
    )