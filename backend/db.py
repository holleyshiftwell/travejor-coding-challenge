import os
import json
import firebase_admin
from firebase_admin import credentials, firestore

def init_firestore():
    key_path = os.getenv("FIREBASE_SERVICE_ACCOUNT")
    key_json = os.getenv("FIREBASE_SERVICE_ACCOUNT_JSON")

    if key_path:
        cred = credentials.Certificate(key_path)
    elif key_json:
        cred_dict = json.loads(key_json)
        cred = credentials.Certificate(cred_dict)
    else:
        raise RuntimeError("Set FIREBASE_SERVICE_ACCOUNT (path) or FIREBASE_SERVICE_ACCOUNT_JSON (content)")
    
    if not firebase_admin._apps:
        firebase_admin.initialize_app(cred)

    return firestore.client()

db = init_firestore()
profiles_col = db.collection("profiles")