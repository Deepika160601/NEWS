from sqlalchemy.ext.asyncio import AsyncSession

from app.utils.api_response import success_response

from app.modules.admin.repositories.dashboard_repository import (
    DashboardRepository
)


class DashboardService:

    @staticmethod
    async def get_dashboard(
        db: AsyncSession
    ):

        dashboard_stats = await DashboardRepository.get_dashboard_stats(
            db
        )

        return success_response(
            "Dashboard data fetched successfully",
            dashboard_stats
        )