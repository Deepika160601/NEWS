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

from app.modules.admin.services.dashboard_service import (
    DashboardService
)

router = APIRouter()


# =========================
# DASHBOARD
# =========================
@router.get("/")
async def get_dashboard(
    db: AsyncSession = Depends(get_db),
    current_admin=Depends(
        get_current_admin
    )
):

    return await DashboardService.get_dashboard(
        db
    )