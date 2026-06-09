from fastapi import (
    APIRouter,
    Depends
)

from sqlalchemy.ext.asyncio import (
    AsyncSession
)

from app.db.db import get_db
from app.core.security import (
    get_current_admin
)

from app.modules.admin.schemas.category_schema import (
    CategoryCreateRequest
)

from app.modules.admin.services.category_service import (
    create_category_service,
    get_all_categories_service,
    delete_category_service
)

router = APIRouter(
    dependencies=[Depends(get_current_admin)]
)


# =========================
# CREATE CATEGORY
# =========================
@router.post("/")
async def add_category(
    data: CategoryCreateRequest,
    db: AsyncSession = Depends(get_db)
):

    return await create_category_service(
        db,
        data
    )


# =========================
# GET ALL CATEGORIES
# =========================
@router.get("/")
async def list_categories(
    db: AsyncSession = Depends(get_db)
):

    return await get_all_categories_service(
        db
    )


# =========================
# DELETE CATEGORY
# =========================
@router.delete("/{category_id}")
async def remove_category(
    category_id: int,
    db: AsyncSession = Depends(get_db)
):

    return await delete_category_service(
        db,
        category_id
    )