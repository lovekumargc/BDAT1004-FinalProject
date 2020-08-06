import pyrebase
from datetime import datetime


class FirebaseClient:
    firebaseConfig = {
        "apiKey": "",
        "authDomain": "",
        "databaseURL": "",
        "storageBucket": "",
        "projectId": "",
        "messagingSenderId": "",
        "appId": "",
        "measurementId": ""
    }

    def __init__(self):
        self.firebase = pyrebase.initialize_app(FirebaseClient.firebaseConfig)

    def getDatabase(self):
        return self.firebase.database()
