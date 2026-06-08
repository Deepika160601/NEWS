from pydantic import BaseModel


# =========================
# SEARCH REQUEST
# =========================
class SearchRequest(
    BaseModel
):

    keyword: str