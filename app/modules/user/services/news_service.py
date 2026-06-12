from fastapi import (
    HTTPException,
    status
)

from sqlalchemy.ext.asyncio import (
    AsyncSession
)

from app.utils.api_response import success_response

from app.utils.location_helper import (
    get_location_from_coordinates
)

from app.modules.user.repositories.news_repository import (
    get_latest_news,
    get_news_by_id
)

from app.modules.user.repositories.user_repository import (
    UserRepository
)


# =========================
# GET LATEST NEWS
# =========================
async def get_latest_news_service(
    db: AsyncSession,
    user_id: int
):

    user = await UserRepository.get_user_by_id(
        db,
        user_id
    )

    if not user:

        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )

    if (
        user.latitude is None or
        user.longitude is None
    ):

        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="User location not available"
        )

    location = await get_location_from_coordinates(
        user.latitude,
        user.longitude
    )

    if not location:

        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Unable to detect location"
        )

    news = await get_latest_news(
        db=db,
        language=user.preferred_language,
        state=location.get("state"),
        district=location.get("district"),
        city=location.get("city")
    )

    if not news:

        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="No news found"
        )

    return success_response(
        "News fetched successfully",
        {
            "language": user.preferred_language,
            "detected_location": location,
            "news": news
        }
    )


# =========================
# GET NEWS DETAILS
# =========================
async def get_news_by_id_service(
    db: AsyncSession,
    news_id: int,
    user_id: int
):

    user = await UserRepository.get_user_by_id(
        db,
        user_id
    )

    if not user:

        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )

    news = await get_news_by_id(
        db=db,
        news_id=news_id,
        language=user.preferred_language
    )

    if not news:

        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="News not found"
        )

    return success_response(
        "News details fetched successfully",
        news
    )