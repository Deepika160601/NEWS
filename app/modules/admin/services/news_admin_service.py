from fastapi import (
    HTTPException,
    status
)

from sqlalchemy.ext.asyncio import (
    AsyncSession
)

from app.modules.admin.repositories.news_admin_repository import (
    create_news,
    get_all_news,
    get_news_by_id,
    publish_news,
    delete_news
)

from app.modules.user.repositories.user_repository import (
    UserRepository
)

from app.modules.user.repositories.notification_repository import (
    create_notification
)


# =========================
# CREATE NEWS
# =========================
async def create_news_service(
    db: AsyncSession,
    data,
    admin_id: int
):

    news_data = data.dict()

    news_data["author_id"] = admin_id

    return await create_news(
        db,
        news_data
    )


# =========================
# GET ALL NEWS
# =========================
async def get_all_news_service(
    db: AsyncSession
):

    return await get_all_news(
        db
    )


# =========================
# GET NEWS BY ID
# =========================
async def get_news_by_id_service(
    db: AsyncSession,
    news_id: int
):

    news = await get_news_by_id(
        db,
        news_id
    )

    if not news:

        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="News not found"
        )

    return news


# =========================
# PUBLISH NEWS
# =========================
async def publish_news_service(
    db: AsyncSession,
    news_id: int
):

    news = await get_news_by_id(
        db,
        news_id
    )

    if not news:

        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="News not found"
        )

    published_news = await publish_news(
        db,
        news
    )

    users = await UserRepository.get_all_users(
        db
    )

    for user in users:

        await create_notification(
            db=db,
            user_id=user.user_id,
            news_id=published_news.news_id,
            title="Breaking News",
            message=published_news.title
        )

    return published_news


# =========================
# DELETE NEWS
# =========================
async def delete_news_service(
    db: AsyncSession,
    news_id: int
):

    news = await get_news_by_id(
        db,
        news_id
    )

    if not news:

        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="News not found"
        )

    await delete_news(
        db,
        news
    )

    return {
        "message": "News deleted successfully"
    }