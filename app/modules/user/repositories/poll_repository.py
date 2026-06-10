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

    polls = result.scalars().all()

    response = []

    for poll in polls:

        total_votes = sum(
            option.votes_count
            for option in poll.options
        )

        response.append(
            {
                "poll_id": poll.poll_id,
                "news_id": poll.news_id,
                "question": poll.question,
                "total_votes": total_votes,
                "created_at": poll.created_at
            }
        )

    return response


## =========================
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

    poll = result.scalar_one_or_none()

    if not poll:
        return None

    options_result = await db.execute(
        select(PollOption).where(
            PollOption.poll_id == poll_id
        )
    )

    options = options_result.scalars().all()

    return {
        "poll_id": poll.poll_id,
        "news_id": poll.news_id,
        "question": poll.question,
        "created_at": poll.created_at,
        "options": [
            {
                "option_id": option.option_id,
                "option_text": option.option_text,
                "votes_count": option.votes_count
            }
            for option in options
        ]
    }


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
# =========================
# GET ALL POLLS
# =========================
async def get_all_polls(
    db: AsyncSession
):

    result = await db.execute(
        select(Poll)
    )

    polls = result.scalars().all()

    return [
        {
            "poll_id": poll.poll_id,
            "news_id": poll.news_id,
            "question": poll.question,
            "created_at": poll.created_at
        }
        for poll in polls
    ]