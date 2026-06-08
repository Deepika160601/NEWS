from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.db.db import (
    engine,
    AsyncSessionLocal
)

from app.models.models import Base

from app.core.admin_initializer import (
    create_default_admin
)


# ========================
# STARTUP
# ========================
@asynccontextmanager
async def lifespan(app: FastAPI):

    # Create Tables
    async with engine.begin() as conn:

        await conn.run_sync(
            Base.metadata.create_all
        )

    # Create Default Admin
    async with AsyncSessionLocal() as db:

        await create_default_admin(
            db
        )

    yield


# ========================
# FASTAPI APP
# ========================
app = FastAPI(
    title="News API",
    description="Backend for News Application",
    version="1.0.0",
    lifespan=lifespan
)


# ========================
# ADMIN ROUTERS
# ========================
from app.modules.admin.auth.admin_router import (
    router as admin_router
)
from app.modules.admin.routers.dashboard_router import router as dashboard_router
from app.modules.admin.routers.category_router import router as category_router
from app.modules.admin.routers.news_admin_router import router as admin_news_router
from app.modules.admin.routers.poll_admin_router import router as admin_poll_router


# ========================
# USER ROUTERS
# ========================
from app.modules.user.routers.user_router import router as user_router
from app.modules.user.routers.news_router import router as user_news_router
from app.modules.user.routers.comment_router import router as comment_router
from app.modules.user.routers.like_router import router as like_router
from app.modules.user.routers.bookmark_router import router as bookmark_router
from app.modules.user.routers.poll_router import router as user_poll_router
from app.modules.user.routers.notification_router import router as notification_router
from app.modules.user.routers.search_router import router as search_router


# ========================
# ADMIN ROUTES
# ========================
app.include_router(
    admin_router,
    prefix="/admin/auth",
    tags=["Admin Authentication"]
)

app.include_router(
    dashboard_router,
    prefix="/admin/dashboard",
    tags=["Admin Dashboard"]
)

app.include_router(
    category_router,
    prefix="/admin/categories",
    tags=["Admin Categories"]
)

app.include_router(
    admin_news_router,
    prefix="/admin/news",
    tags=["Admin News"]
)

app.include_router(
    admin_poll_router,
    prefix="/admin/polls",
    tags=["Admin Polls"]
)


# ========================
# USER ROUTES
# ========================
app.include_router(
    user_router,
    prefix="/auth",
    tags=["User Authentication"]
)

app.include_router(
    user_news_router,
    prefix="/news",
    tags=["News"]
)

app.include_router(
    comment_router,
    prefix="/comments",
    tags=["Comments"]
)

app.include_router(
    like_router,
    prefix="/likes",
    tags=["Likes"]
)

app.include_router(
    bookmark_router,
    prefix="/bookmarks",
    tags=["Bookmarks"]
)

app.include_router(
    user_poll_router,
    prefix="/polls",
    tags=["Polls"]
)

app.include_router(
    notification_router,
    prefix="/notifications",
    tags=["Notifications"]
)

app.include_router(
    search_router,
    prefix="/search",
    tags=["Search"]
)


# ========================
# ROOT
# ========================
@app.get("/")
async def root():

    return {
        "message": "News API is running "
    }