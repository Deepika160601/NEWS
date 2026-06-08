from fastapi import HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.models import User

from app.core.security import (
    hash_password,
    verify_password,
    create_access_token
)

from app.modules.user.repositories.user_repository import (
    UserRepository
)


class UserService:

    # =========================
    # REGISTER USER
    # =========================
    @staticmethod
    async def register_user(
        db: AsyncSession,
        name: str,
        email: str,
        mobile_number: str,
        password: str
    ):

        existing_user = await UserRepository.get_user_by_email(
            db,
            email
        )

        if existing_user:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Email already registered"
            )

        user = User(
            name=name,
            email=email,
            mobile_number=mobile_number,
            password_hash=hash_password(password)
        )

        return await UserRepository.create_user(
            db,
            user
        )

    # =========================
    # LOGIN USER
    # =========================
    @staticmethod
    async def login_user(
        db: AsyncSession,
        email: str,
        password: str
    ):

        user = await UserRepository.get_user_by_email(
            db,
            email
        )

        if not user:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="User not found"
            )

        if not verify_password(
            password,
            user.password_hash
        ):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid credentials"
            )

        access_token = create_access_token(
            {
                "user_id": user.user_id,
                "email": user.email,
                "role": "user"
            }
        )

        return {
            "access_token": access_token,
            "token_type": "bearer"
        }

    # =========================
    # GET PROFILE
    # =========================
    @staticmethod
    async def get_profile(
        db: AsyncSession,
        user_id: int
    ):

        user = await UserRepository.get_user_by_id(
            db,
            user_id
        )

        if not user:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="User not found"
            )

        return user

    # =========================
    # UPDATE LANGUAGE
    # =========================
    @staticmethod
    async def update_language(
        db: AsyncSession,
        user_id: int,
        preferred_language: str
    ):

        user = await UserRepository.get_user_by_id(
            db,
            user_id
        )

        if not user:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="User not found"
            )

        user.preferred_language = preferred_language

        await db.commit()
        await db.refresh(user)

        return {
            "message": "Language updated successfully",
            "preferred_language": user.preferred_language
        }