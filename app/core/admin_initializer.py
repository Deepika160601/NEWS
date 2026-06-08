from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.models import Admin
from app.core.config import settings
from app.core.security import hash_password


async def create_default_admin(
    db: AsyncSession
):

    result = await db.execute(
        select(Admin).where(
            Admin.email ==
            settings.DEFAULT_ADMIN_EMAIL
        )
    )

    admin = result.scalar_one_or_none()

    if admin:
        print("Admin already exists")
        return

    admin = Admin(
        name=settings.DEFAULT_ADMIN_NAME,
        email=settings.DEFAULT_ADMIN_EMAIL,
        password_hash=hash_password(
            settings.DEFAULT_ADMIN_PASSWORD
        ),
        role=settings.DEFAULT_ADMIN_ROLE
    )

    db.add(admin)

    await db.commit()

    print(
        "Default admin created successfully"
    )