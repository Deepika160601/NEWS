from pydantic import BaseModel
from typing import List


# =========================
# CREATE POLL REQUEST
# =========================
class PollCreateRequest(BaseModel):

    news_id: int

    question: str

    options: List[str]


# =========================
# POLL RESPONSE
# =========================
class PollResponse(BaseModel):

    poll_id: int

    news_id: int

    question: str

    class Config:
        from_attributes = True


# =========================
# POLL OPTION RESPONSE
# =========================
class PollOptionResponse(BaseModel):

    option_id: int

    option_text: str

    votes_count: int

    class Config:
        from_attributes = True