from sqlalchemy.ext.asyncio import AsyncSession

from app.modules.admin.repositories.dashboard_repository import (
    DashboardRepository
)


class DashboardService:

    @staticmethod
    async def get_dashboard(
        db: AsyncSession
    ):

        return await DashboardRepository.get_dashboard_stats(
            db
        )