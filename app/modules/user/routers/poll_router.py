from fastapi import (
    APIRouter,
    Depends
)

from sqlalchemy.ext.asyncio import (
    AsyncSession
)

from app.db.db import get_db

from app.core.security import (
    get_current_user
)

from app.modules.user.schemas.poll_schema import (
    PollVoteRequest
)

from app.modules.user.services.poll_service import (
    get_all_polls_service,
    get_poll_by_id_service,
    vote_poll_service
)

router = APIRouter()


# =========================
# GET ALL POLLS
# =========================
@router.get("/")
async def get_polls(
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
# VOTE POLL
# =========================
@router.post("/vote")
async def vote(
    data: PollVoteRequest,
    db: AsyncSession = Depends(get_db),
    current_user=Depends(get_current_user)
):

    return await vote_poll_service(
        db,
        data.poll_id,
        data.option_id,
        current_user["user_id"]
    )