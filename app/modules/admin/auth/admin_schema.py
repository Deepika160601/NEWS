from pydantic import BaseModel, EmailStr


class AdminLoginRequest(BaseModel):
    email: EmailStr
    password: str


class AdminLoginResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"


class AdminProfileResponse(BaseModel):
    admin_id: int
    name: str
    email: str
    role: str

    class Config:
        from_attributes = True