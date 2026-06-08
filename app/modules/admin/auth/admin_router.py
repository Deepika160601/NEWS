from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.db import get_db

from app.modules.admin.auth.admin_schema import (
    AdminLoginRequest
)

from app.modules.admin.auth.admin_service import (
    AdminService
)

router = APIRouter()


# =========================
# ADMIN LOGIN
# =========================
@router.post("/login")
async def login_admin(
    request: AdminLoginRequest,
    db: AsyncSession = Depends(get_db)
):

    return await AdminService.login_admin(
        db,
        request.email,
        request.password
    )
