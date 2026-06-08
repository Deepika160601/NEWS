from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.models import Category


# =========================
# CREATE CATEGORY
# =========================
async def create_category(
    db: AsyncSession,
    name: str,
    description: str
):

    category = Category(
        name=name,
        description=description
    )

    db.add(category)

    await db.commit()

    await db.refresh(category)

    return category


# =========================
# GET CATEGORY BY NAME
# =========================
async def get_category_by_name(
    db: AsyncSession,
    name: str
):

    result = await db.execute(
        select(Category).where(
            Category.name == name
        )
    )

    return result.scalar_one_or_none()


# =========================
# GET CATEGORY BY ID
# =========================
async def get_category_by_id(
    db: AsyncSession,
    category_id: int
):

    result = await db.execute(
        select(Category).where(
            Category.category_id == category_id
        )
    )

    return result.scalar_one_or_none()


# =========================
# GET ALL CATEGORIES
# =========================
async def get_all_categories(
    db: AsyncSession
):

    result = await db.execute(
        select(Category)
    )

    return result.scalars().all()


# =========================
# DELETE CATEGORY
# =========================
async def delete_category(
    db: AsyncSession,
    category: Category
):

    await db.delete(category)

    await db.commit()