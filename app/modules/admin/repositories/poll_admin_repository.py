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
# DELETE POLL
# =========================
async def delete_poll(
    db: AsyncSession,
    poll: Poll
):

    await db.delete(poll)

    await db.commit()