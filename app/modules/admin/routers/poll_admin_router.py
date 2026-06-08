from fastapi import (
    APIRouter,
    Depends,
    HTTPException
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

from app.modules.admin.repositories.poll_admin_repository import (
    create_poll,
    get_poll_by_id,
    get_all_polls,
    delete_poll
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

    if len(data.options) < 2:

        raise HTTPException(
            status_code=400,
            detail="At least 2 options required"
        )

    return await create_poll(
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

    return await get_all_polls(
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

    poll = await get_poll_by_id(
        db,
        poll_id
    )

    if not poll:

        raise HTTPException(
            status_code=404,
            detail="Poll not found"
        )

    return poll


# =========================
# DELETE POLL
# =========================
@router.delete("/{poll_id}")
async def remove_poll(
    poll_id: int,
    db: AsyncSession = Depends(get_db)
):

    poll = await get_poll_by_id(
        db,
        poll_id
    )

    if not poll:

        raise HTTPException(
            status_code=404,
            detail="Poll not found"
        )

    await delete_poll(
        db,
        poll
    )

    return {
        "message": "Poll deleted successfully"
    }