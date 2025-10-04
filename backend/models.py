from pydantic import BaseModel, EmailStr, Field
from typing import List, Optional

class ProfileBase(BaseModel):
    username: str = Field(..., min_length=1)
    email: EmailStr
    bio: Optional[str] = Field(default="")
    interests: Optional[List[str]] = Field(default=[])
    location: Optional[str] = Field(default="")
    avatarURL: Optional[str] = None

class ProfileResponse(BaseModel):
    id: str
    createdAt: str
    updatedAt: str

class ProfileUpdate(BaseModel):
    bio: Optional[str] = None
    interests: Optional[List[str]] = None