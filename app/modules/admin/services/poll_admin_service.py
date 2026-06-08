from fastapi import (
    HTTPException,
    status
)

from sqlalchemy.ext.asyncio import (
    AsyncSession
)

from app.modules.admin.repositories.poll_admin_repository import (
    create_poll,
    get_all_polls,
    get_poll_by_id,
    delete_poll
)


# =========================
# CREATE POLL
# =========================
async def create_poll_service(
    db: AsyncSession,
    data
):

    if len(data.options) < 2:

        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="At least 2 options required"
        )

    return await create_poll(
        db,
        data
    )


# =========================
# GET ALL POLLS
# =========================
async def get_all_polls_service(
    db: AsyncSession
):

    return await get_all_polls(
        db
    )


# =========================
# GET POLL BY ID
# =========================
async def get_poll_by_id_service(
    db: AsyncSession,
    poll_id: int
):

    poll = await get_poll_by_id(
        db,
        poll_id
    )

    if not poll:

        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Poll not found"
        )

    return poll


# =========================
# DELETE POLL
# =========================
async def delete_poll_service(
    db: AsyncSession,
    poll_id: int
):

    poll = await get_poll_by_id(
        db,
        poll_id
    )

    if not poll:

        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Poll not found"
        )

    await delete_poll(
        db,
        poll
    )

    return {
        "message":
        "Poll deleted successfully"
    }