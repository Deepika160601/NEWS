from pydantic import BaseModel


class DashboardResponse(BaseModel):

    total_users: int

    total_news: int

    published_news: int

    draft_news: int

    total_categories: int

    total_polls: int