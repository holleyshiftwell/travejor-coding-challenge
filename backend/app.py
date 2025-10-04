import os
import uuid
from datetime import datetime, timezone
from typing import Optional, List
from fastapi import FastAPI, HTTPException, Depends, Header, status
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from google.api_core.exceptions import NotFound
import jwt

from dotenv import load_dotenv
load_dotenv()

from db import profiles_col
from models import ProfileBase, ProfileResponse, ProfileUpdate

app = FastAPI(title="Travejor Profile API")

#CORS - allow localhost dev frontends
allowed = os.getenv("ALLOWED_ORIGINS", "http://localhost:5500").split(",")
app.add_middleware(
    CORSMiddleware,
    allow_origins=allowed,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount("/", StaticFiles(directory="../frontend", html=True), name="frontend")

JWT_SECRET = os.getenv("JWT_SECRET")

def now_iso():
    return datetime.now(timezone.utc).isoformat()

def verify_jwt(authorization: Optional[str] = Header(None)) -> str:
    if not JWT_SECRET:
        None
    
    if not authorization:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Missing Authorization header")
    
    parts = authorization.split()
    if parts[0].lower() != "bearer" or len(parts) != 2:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid Authorization header format")
    
    token = parts[1]
    try:
        payload = jwt.decode(token, JWT_SECRET, algorithms=["HS256"])
        return payload
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token has expired")
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=401, detail="Invalid token")
    
@app.post("/api/profiles", response_model=ProfileResponse, status_code=201)
def create_profile(p: ProfileBase):
    existing = profiles_col.where("username", "==", p.username).limit(1).get()
    if existing:
        raise HTTPException(status_code=400, detail="Username already exists")
    
    #to generate a unique ID
    profile_id = f"trav_{uuid.uuid4().hex[:8]}"
    timestamp = now_iso()

    doc = {
        "username": p.username,
        "email": p.email,
        "bio": p.bio or "",
        "interests": p.interests or [],
        "location": p.location or "",
        "avatarURL": p.avatarURL or "",
        "createdAt": timestamp,
        "updatedAt": timestamp,
    }

    profiles_col.document(profile_id).set(doc)
    doc["id"] = profile_id
    return doc

@app.get("/api/profiles/{profile_id}", response_model=ProfileResponse)
def get_profile(profile_id: str):
    doc = profiles_col.document(profile_id).get()
    if not doc.exists:
        raise HTTPException(status_code=404, detail="Profile not found")
    
    data = doc.to_dict()
    data["id"] = profile_id
    return data

@app.put("/api/profiles/{profile_id}", response_model=ProfileResponse)
def update_profile(profile_id: str, update: ProfileUpdate):
    try:
        doc_ref = profiles_col.document(profile_id)
        doc = doc_ref.get()
        if not doc.exists:
            raise HTTPException(status_code=404, detail="Profile not found")
        
    except NotFound:
        raise HTTPException(status_code=404, detail="Profile not found")
    
    update_data = {}
    if update.bio is not None:
        update_data["bio"] = update.bio
    if update.interests is not None:
        update_data["interests"] = update.interests

    if not update_data:
        raise HTTPException(status_code=400, detail="No valid fields to update")
    
    update_data["updatedAt"] = now_iso()
    doc_ref.update(update_data)

    new_doc = doc_ref.get().to_dict()
    new_doc["id"] = profile_id
    return new_doc