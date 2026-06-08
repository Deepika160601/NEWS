from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.models import Admin


class AdminRepository:

    @staticmethod
    async def get_admin_by_email(
        db: AsyncSession,
        email: str
    ):

        result = await db.execute(
            select(Admin).where(
                Admin.email == email
            )
        )

        return result.scalar_one_or_none()

    @staticmethod
    async def get_admin_by_id(
        db: AsyncSession,
        admin_id: int
    ):

        result = await db.execute(
            select(Admin).where(
                Admin.admin_id == admin_id
            )
        )

        return result.scalar_one_or_none()