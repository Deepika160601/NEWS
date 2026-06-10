from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.models import (
    Poll,
    PollOption
)


# =========================
# CREATE POLL
# =========================
async def create_poll(
    db: AsyncSession,
    data
):

    poll = Poll(
        news_id=data.news_id,
        question=data.question
    )

    db.add(poll)

    await db.commit()

    await db.refresh(poll)

    for opt in data.options:

        option = PollOption(
            poll_id=poll.poll_id,
            option_text=opt
        )

        db.add(option)

    await db.commit()

    await db.refresh(poll)

    return poll


# =========================
# GET POLL BY NEWS ID
# =========================
async def get_poll_by_news_id(
    db: AsyncSession,
    news_id: int
):

    result = await db.execute(
        select(Poll).where(
            Poll.news_id == news_id
        )
    )

    return result.scalars().first()


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

    poll = result.scalar_one_or_none()

    if not poll:
        return None

    result = await db.execute(
        select(PollOption).where(
            PollOption.poll_id == poll_id
        )
    )

    options = result.scalars().all()

    return {
        "poll_id": poll.poll_id,
        "news_id": poll.news_id,
        "question": poll.question,
        "options": [
            {
                "option_id": option.option_id,
                "option_text": option.option_text,
                "votes_count": option.votes_count
            }
            for option in options
        ],
        "created_at": poll.created_at
    }

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


# =========================
# DELETE POLL
# =========================
async def delete_poll(
    db: AsyncSession,
    poll: Poll
):

    result = await db.execute(
        select(Poll).where(
            Poll.poll_id == poll["poll_id"]
        )
    )

    poll_obj = result.scalar_one_or_none()

    if poll_obj:

        await db.delete(poll_obj)

        await db.commit()