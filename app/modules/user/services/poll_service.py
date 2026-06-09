from fastapi import (
    HTTPException,
    status
)

from sqlalchemy.ext.asyncio import (
    AsyncSession
)

from app.utils.api_response import success_response

from app.modules.user.repositories.poll_repository import (
    get_all_polls,
    get_poll_by_id,
    get_user_vote,
    vote_poll
)


# =========================
# GET ALL POLLS
# =========================
async def get_all_polls_service(
    db: AsyncSession
):

    polls = await get_all_polls(
        db
    )

    return success_response(
        "Polls fetched successfully",
        polls
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

    return success_response(
        "Poll fetched successfully",
        poll
    )


# =========================
# VOTE POLL
# =========================
async def vote_poll_service(
    db: AsyncSession,
    poll_id: int,
    option_id: int,
    user_id: int
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

    existing_vote = await get_user_vote(
        db,
        poll_id,
        user_id
    )

    if existing_vote:

        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="You have already voted"
        )

    vote = await vote_poll(
        db,
        poll_id,
        option_id,
        user_id
    )

    return success_response(
        "Vote submitted successfully",
        vote
    )