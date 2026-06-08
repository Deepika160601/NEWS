from fastapi import HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.security import (
    verify_password,
    create_access_token
)

from app.modules.admin.auth.admin_repository import (
    AdminRepository
)

class AdminService:

    @staticmethod
    async def login_admin(
        db: AsyncSession,
        email: str,
        password: str
    ):

        admin = await AdminRepository.get_admin_by_email(
            db,
            email
        )

        if not admin:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Admin not found"
            )

        if not verify_password(
            password,
            admin.password_hash
        ):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid credentials"
            )

        token = create_access_token(
            {
                "admin_id": admin.admin_id,
                "email": admin.email,
                "role": admin.role
            }
        )

        return {
            "access_token": token,
            "token_type": "bearer"
        }

    @staticmethod
    async def get_profile(
        db: AsyncSession,
        admin_id: int
    ):

        admin = await AdminRepository.get_admin_by_id(
            db,
            admin_id
        )

        if not admin:
            raise HTTPException(
                status_code=404,
                detail="Admin not found"
            )

        return admin