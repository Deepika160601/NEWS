from pydantic import BaseModel


# =========================
# VOTE REQUEST
# =========================
class PollVoteRequest(
    BaseModel
):

    poll_id: int

    option_id: int



# =========================
# POLL RESPONSE
# =========================
class PollResponse(
    BaseModel
):

    poll_id: int

    news_id: int

    question: str

    class Config:
        from_attributes = True