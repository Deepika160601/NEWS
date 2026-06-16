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

from app.modules.user.services.news_service import (
    get_latest_news_service,
    get_news_by_id_service,
      share_news_service
)

router = APIRouter()


# =========================
# GET LATEST NEWS
# =========================
@router.get("/")
async def latest_news(
    db: AsyncSession = Depends(get_db),
    current_user=Depends(get_current_user)
):

    return await get_latest_news_service(
        db,
        current_user["user_id"]
    )


# =========================
# GET NEWS DETAILS
# =========================
@router.get("/{news_id}")
async def news_details(
    news_id: int,
    db: AsyncSession = Depends(get_db),
    current_user=Depends(get_current_user)
):

    return await get_news_by_id_service(
        db,
        news_id,
        current_user["user_id"]
    )
# =========================
# SHARE NEWS
# =========================
@router.get("/{news_id}/share")
async def share_news_api(
    news_id: int,
    db: AsyncSession = Depends(get_db)
):

    return await share_news_service(
        db,
        news_id
    )