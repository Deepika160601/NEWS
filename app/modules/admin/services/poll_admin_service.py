from fastapi import (
    HTTPException,
    status
)

from sqlalchemy.ext.asyncio import (
    AsyncSession
)

from sqlalchemy import select

from app.models.models import News

from app.utils.api_response import success_response

from app.modules.admin.repositories.poll_admin_repository import (
    create_poll,
    get_all_polls,
    get_poll_by_id,
    get_poll_by_news_id,
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

    result = await db.execute(
        select(News).where(
            News.news_id == data.news_id
        )
    )

    news = result.scalar_one_or_none()

    if not news:

        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="News not found"
        )

    existing_poll = await get_poll_by_news_id(
        db,
        data.news_id
    )

    if existing_poll:

        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Poll already exists for this news"
        )

    poll = await create_poll(
        db,
        data
    )

    return success_response(
        "Poll created successfully",
        poll
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

    return success_response(
        "Poll deleted successfully",
        {
            "poll_id": poll_id
        }
    )