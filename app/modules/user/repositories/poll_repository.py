from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.models import (
    Poll,
    PollOption,
    PollVote
)


# =========================
# GET ALL POLLS
# =========================
async def get_all_polls(
    db: AsyncSession
):

    result = await db.execute(
        select(Poll)
    )

    return result.scalars().all()


# =========================
# GET POLL BY ID
# =========================
async def get_poll_by_id(
    db: AsyncSession,
    poll_id: int
):

    result = await db.execute(
        select(Poll).where(
            Poll.poll_id == poll_id
        )
    )

    return result.scalar_one_or_none()


# =========================
# CHECK USER VOTE
# =========================
async def get_user_vote(
    db: AsyncSession,
    poll_id: int,
    user_id: int
):

    result = await db.execute(
        select(PollVote).where(
            PollVote.poll_id == poll_id,
            PollVote.user_id == user_id
        )
    )

    return result.scalar_one_or_none()


# =========================
# VOTE POLL
# =========================
async def vote_poll(
    db: AsyncSession,
    poll_id: int,
    option_id: int,
    user_id: int
):

    vote = PollVote(
        poll_id=poll_id,
        option_id=option_id,
        user_id=user_id
    )

    db.add(vote)

    result = await db.execute(
        select(PollOption).where(
            PollOption.option_id == option_id
        )
    )

    option = result.scalar_one_or_none()

    if option:
        option.votes_count += 1

    await db.commit()

    await db.refresh(vote)

    return vote