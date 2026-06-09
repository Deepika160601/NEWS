from fastapi import (
    HTTPException,
    status
)

from sqlalchemy.ext.asyncio import (
    AsyncSession
)

from app.utils.api_response import success_response

from app.modules.admin.repositories.category_repository import (
    create_category,
    get_category_by_name,
    get_category_by_id,
    get_all_categories,
    delete_category
)


# =========================
# CREATE CATEGORY
# =========================
async def create_category_service(
    db: AsyncSession,
    data
):

    existing = await get_category_by_name(
        db,
        data.name
    )

    if existing:

        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Category already exists"
        )

    category = await create_category(
        db,
        data.name,
        data.description
    )

    return success_response(
        "Category created successfully",
        category
    )


# =========================
# GET ALL CATEGORIES
# =========================
async def get_all_categories_service(
    db: AsyncSession
):

    categories = await get_all_categories(
        db
    )

    return success_response(
        "Categories fetched successfully",
        categories
    )


# =========================
# DELETE CATEGORY
# =========================
async def delete_category_service(
    db: AsyncSession,
    category_id: int
):

    category = await get_category_by_id(
        db,
        category_id
    )

    if not category:

        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Category not found"
        )

    await delete_category(
        db,
        category
    )

    return success_response(
        "Category deleted successfully"
    )