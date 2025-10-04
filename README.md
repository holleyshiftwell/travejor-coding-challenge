# travejor-coding-challenge
backend developer coding challenge (revised: API + visual profile page)

# TECH STACK:
Frontend: HTML, CSS, JavaScript
Backend: Python, FastAPI, uvicorn
Environment Management: Python venv & dot-env

# ENVIRONMENT VARIABLES:
FIREBASE_SERVICE_ACCOUNT=backend/firebaseadminsdk.json
ALLOWED_ORIGINS=http://localhost:5500

# SETUP STEPS:
1. Clone the repo
git clone https://github.com/holleyshiftwell/travejor-coding-challenge.git
cd travejor-coding-challenge

2. Activate virtual environment
cd backend
python -m venv venv
venv\Scripts\activate #this is the activation for windows
source venv/bin/activate #this is the activation for mac
pip install -r requirements.txt

3. Configure environment
FIREBASE_SERVICE_ACCOUNT=backend/firebaseadminsdk.json
ALLOWED_ORIGINS=http://localhost:5500

4. Seed Firestore (there are already seeds in firestore, but you can add some more using this template)
from db import profiles_col

profiles_col.document("trav_test1").set({
    "username": "traveler1",
    "email": "trav1@example.com",
    "bio": "Love traveling the world!",
    "interests": ["hiking", "photography"],
    "location": "Paris, France",
    "avatarURL": ""
})

# RUNNING THE BACKEND:
cd backend
venv\Scripts\activate 

uvicorn app:app --reload

Backend will run at: http://127.0.0.1:8000
API docs are available at: http://127.0.0.1:8000/docs

# RUNNING THE FRONTEND:
const API_BASE = "http://127.0.0.1:8000/api"; // backend URL


