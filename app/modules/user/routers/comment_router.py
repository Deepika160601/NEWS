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

from app.modules.user.schemas.comment_schema import (
    CommentCreateRequest
)

from app.modules.user.services.comment_service import (
    add_comment_service,
    get_comments_service
)

router = APIRouter()


# =========================
# ADD COMMENT
# =========================
@router.post("/")
async def create_comment(
    data: CommentCreateRequest,
    db: AsyncSession = Depends(get_db),
    current_user=Depends(get_current_user)
):

    return await add_comment_service(
        db,
        data,
        current_user["user_id"]
    )


# =========================
# GET COMMENTS BY NEWS
# =========================
@router.get("/{news_id}")
async def get_comments(
    news_id: int,
    db: AsyncSession = Depends(get_db)
):

    return await get_comments_service(
        db,
        news_id
    )