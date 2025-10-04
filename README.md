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

# RUNNING THE BACKEND:
cd backend
venv\Scripts\activate 

uvicorn app:app --reload

Backend will run at: http://127.0.0.1:8000
API docs are available at: http://127.0.0.1:8000/docs

# RUNNING THE FRONTEND:
const API_BASE = "http://127.0.0.1:8000/api"; // backend URL

# DEMO POST, GET, and PUT Endpoints via http://127.0.0.1:8000/docs
POST:
    - Click on POST
    - Click "Try it out"
    - Alter the values, then click execute. On the terminal, you'll be able to see that the database was successfully updated if the username is unique.
If the username is not unique, you will get an error
    - Under the code details still on the docs website, you'll be able to find the "id", which you can use to test the GET and PUT endpoints

GET:
    - Click on GET
    - Click "Try it out"
    - Input the profile id (that you got from the last step of the POST testing)
    - You will be able to view the values for the attributes of that specific ID in the docs. Additionally on the terminal, you'll be able to see that the database was able to retrieve the information if the id exists. If the username does not exist, you will get an error.

PUT:
    - Click on PUT
    - Click "Try it out"
    - Input the profile id (that you got from the last step of the POST testing)
    - You will be able to edit the values for bio and interests. Additionally on the terminal, you'll be able to see that the database was able to retrieve and update the information if the id exists. If the username does not exist, you will get an error.


# DEMO Frontend Profile Page http://127.0.0.1:8000/index.html

Input any or all of the following travejor IDs. They should have the respective values, of which the bio and interests are immutable. Additionally, the updatedAt value will update when the button to update is clicked. (do not include the brackets or anything outside it. it should follow the form of trav_xxxxxxxx)

# <trav_eb5b6b94>
{
avatarURL
"string"
(string)

bio
"i want this job <3"
(string)

createdAt
"2025-10-04T10:06:44.339410+00:00"
(string)

email
"gimmejob@gmail.com"
(string)

interests
(array)

1 "getting a job"
(string)

2 "getting hired"
(string)

location
"New York, USA"
(string)

updatedAt
"2025-10-04T10:07:25.516664+00:00"
(string)

username
"pleasegivemethisjob"}

# <trav_e3d05c1c>
{
avatarURL
"job"
(string)

bio
"please hire me"
(string)

createdAt
"2025-10-04T10:14:50.530207+00:00"

email
"want2work@gmail.com"
(string)

interests
(array)

1 "working smart"
(string)

2 "working hard"
(string)

location
"Cebu, Philippines"
(string)

updatedAt
"2025-10-04T12:35:57.736900+00:00"

username
"hireMePls"
}

# <trav_dff57ea9>
{
    avatarURL
":O"
(string)

bio
"i want to be a software engineer"
(string)

createdAt
"2025-10-04T10:01:17.942271+00:00"

email
"ilovecoding@gmail.com"
(string)

interests
(array)

0
"backend"

1
"python"

2
"firebase"


location
"Manila, Philippines"

updatedAt
"2025-10-04T10:01:17.942271+00:00"

username
"coder"
}

Thank you for your time! I hope I was able to meet the expectations.


