from fastapi import (
    APIRouter,
    Depends,
    Form
)

from sqlalchemy.ext.asyncio import (
    AsyncSession
)

from app.db.db import get_db

from app.core.security import (
    get_current_admin
)

from app.modules.admin.schemas.news_admin_schema import (
    NewsCreateRequest
)

from app.modules.admin.services.news_admin_service import (
    create_news_service,
    get_all_news_service,
    publish_news_service,
    delete_news_service,
    get_news_by_id_service
)

router = APIRouter(
    dependencies=[Depends(get_current_admin)]
)


# =========================
# CREATE NEWS
# =========================
@router.post("/")
async def add_news(
    title: str = Form(...),
    content: str = Form(...),
    summary: str = Form(None),
    category_id: int = Form(...),
    location_id: int = Form(...),
    is_breaking: bool = Form(False),
    thumbnail_url: str = Form(None),
    video_url: str = Form(None),   # <-- ADD THIS
    db: AsyncSession = Depends(get_db),
    current_admin=Depends(get_current_admin)
):

    data = NewsCreateRequest(
        title=title,
        content=content,
        summary=summary,
        category_id=category_id,
        location_id=location_id,
        is_breaking=is_breaking,
        thumbnail_url=thumbnail_url
    )

    return await create_news_service(
        db,
        data,
        current_admin["admin_id"]
    )


# =========================
# GET ALL NEWS
# =========================
@router.get("/")
async def list_news(
    db: AsyncSession = Depends(get_db)
):

    return await get_all_news_service(
        db
    )


# =========================
# GET NEWS BY ID
# =========================
@router.get("/{news_id}")
async def get_news(
    news_id: int,
    db: AsyncSession = Depends(get_db)
):

    return await get_news_by_id_service(
        db,
        news_id
    )


# =========================
# PUBLISH NEWS
# =========================
@router.put("/publish/{news_id}")
async def publish_news(
    news_id: int,
    db: AsyncSession = Depends(get_db)
):

    return await publish_news_service(
        db,
        news_id
    )


# =========================
# DELETE NEWS
# =========================
@router.delete("/{news_id}")
async def remove_news(
    news_id: int,
    db: AsyncSession = Depends(get_db)
):

    return await delete_news_service(
        db,
        news_id
    )