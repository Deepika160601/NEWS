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

from app.modules.admin.schemas.poll_admin_schema import (
    PollCreateRequest
)

from app.modules.admin.services.poll_admin_service import (
    create_poll_service,
    get_all_polls_service,
    get_poll_by_id_service,
    delete_poll_service
)

router = APIRouter(
    dependencies=[
        Depends(get_current_admin)
    ]
)


# =========================
# CREATE POLL
# =========================
@router.post("/")
async def add_poll(
    data: PollCreateRequest,
    db: AsyncSession = Depends(get_db)
):

    return await create_poll_service(
        db,
        data
    )


# =========================
# GET ALL POLLS
# =========================
@router.get("/")
async def list_polls(
    db: AsyncSession = Depends(get_db)
):

    return await get_all_polls_service(
        db
    )


# =========================
# GET POLL BY ID
# =========================
@router.get("/{poll_id}")
async def get_poll(
    poll_id: int,
    db: AsyncSession = Depends(get_db)
):

    return await get_poll_by_id_service(
        db,
        poll_id
    )


# =========================
# DELETE POLL
# =========================
@router.delete("/{poll_id}")
async def remove_poll(
    poll_id: int,
    db: AsyncSession = Depends(get_db)
):

    return await delete_poll_service(
        db,
        poll_id
    )