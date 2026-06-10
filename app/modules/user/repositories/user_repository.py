from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.models import User


class UserRepository:

    # =========================
    # GET BY EMAIL
    # =========================
    @staticmethod
    async def get_user_by_email(
        db: AsyncSession,
        email: str
    ):

        result = await db.execute(
            select(User).where(
                User.email == email
            )
        )

        return result.scalar_one_or_none()

    # =========================
    # GET BY MOBILE NUMBER
    # =========================
    @staticmethod
    async def get_user_by_mobile_number(
        db: AsyncSession,
        mobile_number: str
    ):

        result = await db.execute(
            select(User).where(
                User.mobile_number == mobile_number
            )
        )

        return result.scalar_one_or_none()

    # =========================
    # GET BY ID
    # =========================
    @staticmethod
    async def get_user_by_id(
        db: AsyncSession,
        user_id: int
    ):

        result = await db.execute(
            select(User).where(
                User.user_id == user_id
            )
        )

        return result.scalar_one_or_none()

    # =========================
    # CREATE USER
    # =========================
    @staticmethod
    async def create_user(
        db: AsyncSession,
        user: User
    ):

        db.add(user)

        await db.commit()

        await db.refresh(user)

        return user

    # =========================
    # UPDATE LANGUAGE
    # =========================
    @staticmethod
    async def update_user_language(
        db: AsyncSession,
        user_id: int,
        preferred_language: str
    ):

        result = await db.execute(
            select(User).where(
                User.user_id == user_id
            )
        )

        user = result.scalar_one_or_none()

        if not user:
            return None

        user.preferred_language = preferred_language

        await db.commit()

        await db.refresh(user)

        return user

    # =========================
    # GET ALL USERS
    # =========================
    @staticmethod
    async def get_all_users(
        db: AsyncSession
    ):

        result = await db.execute(
            select(User)
        )

        return result.scalars().all()