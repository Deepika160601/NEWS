from fastapi import (
    APIRouter,
    Depends
)

from sqlalchemy.ext.asyncio import (
    AsyncSession
)

from app.db.db import get_db

from app.core.security import (
    get_current_user
)

from app.modules.user.schemas.bookmark_schema import (
    BookmarkCreateRequest
)

from app.modules.user.services.bookmark_service import (
    add_bookmark_service,
    get_user_bookmarks_service,
    remove_bookmark_service
)

router = APIRouter(
    dependencies=[
        Depends(get_current_user)
    ]
)


# =========================
# ADD BOOKMARK
# =========================
@router.post("/")
async def add_user_bookmark(
    data: BookmarkCreateRequest,
    db: AsyncSession = Depends(get_db),
    current_user=Depends(get_current_user)
):

    return await add_bookmark_service(
        db,
        current_user["user_id"],
        data.news_id
    )


# =========================
# GET MY BOOKMARKS
# =========================
@router.get("/")
async def get_bookmarks(
    db: AsyncSession = Depends(get_db),
    current_user=Depends(get_current_user)
):

    return await get_user_bookmarks_service(
        db,
        current_user["user_id"]
    )


# =========================
# REMOVE BOOKMARK
# =========================
@router.delete("/{news_id}")
async def delete_bookmark(
    news_id: int,
    db: AsyncSession = Depends(get_db),
    current_user=Depends(get_current_user)
):

    return await remove_bookmark_service(
        db,
        current_user["user_id"],
        news_id
    )