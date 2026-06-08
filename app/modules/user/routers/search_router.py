from fastapi import (
    APIRouter,
    Depends
)

from sqlalchemy.ext.asyncio import (
    AsyncSession
)

from app.db.db import get_db

from app.modules.user.services.search_service import (
    search_news_service
)

router = APIRouter()


# =========================
# SEARCH NEWS
# =========================
@router.get("/")
async def search(
    keyword: str,
    db: AsyncSession = Depends(get_db)
):

    return await search_news_service(
        db,
        keyword
    )