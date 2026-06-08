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

from app.modules.user.schemas.like_schema import (
    LikeRequest
)

from app.modules.user.services.like_service import (
    like_news_service,
    unlike_news_service
)

router = APIRouter()


# =========================
# LIKE NEWS
# =========================
@router.post("/")
async def like_news_api(
    data: LikeRequest,
    db: AsyncSession = Depends(get_db),
    current_user=Depends(get_current_user)
):

    return await like_news_service(
        db,
        current_user["user_id"],
        data.news_id
    )


# =========================
# UNLIKE NEWS
# =========================
@router.delete("/{news_id}")
async def unlike_news_api(
    news_id: int,
    db: AsyncSession = Depends(get_db),
    current_user=Depends(get_current_user)
):

    return await unlike_news_service(
        db,
        current_user["user_id"],
        news_id
    )