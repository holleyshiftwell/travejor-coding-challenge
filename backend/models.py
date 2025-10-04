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
    username: str
    email: str
    bio: Optional[str] = ""
    interests: Optional[List[str]] = []
    location: Optional[str] = ""
    avatarURL: Optional[str] = None
    createdAt: str
    updatedAt: str

class ProfileUpdate(BaseModel):
    bio: Optional[str] = None
    interests: Optional[List[str]] = None