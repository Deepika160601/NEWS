from pydantic import BaseModel, EmailStr
from typing import Literal


# =========================
# REGISTER
# =========================
class UserRegisterRequest(BaseModel):
    name: str
    email: EmailStr
    mobile_number: str
    password: str


# =========================
# LOGIN
# =========================
class UserLoginRequest(BaseModel):
    email: EmailStr
    password: str


# =========================
# TOKEN RESPONSE
# =========================
class TokenResponse(BaseModel):
    access_token: str
    token_type: str


# =========================
# USER RESPONSE
# =========================
class UserResponse(BaseModel):
    user_id: int
    name: str
    email: str
    mobile_number: str
    preferred_language: str

    class Config:
        from_attributes = True


# =========================
# UPDATE LANGUAGE
# =========================
class LanguageUpdateRequest(BaseModel):
    preferred_language: Literal[
        "en",
        "te",
        "hi",
        "ta",
        "kn"
    ]