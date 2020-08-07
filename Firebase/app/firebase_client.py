import pyrebase
from datetime import datetime


class FirebaseClient:
    firebaseConfig = {
        "apiKey": "AIzaSyCZdJSflZ-287I7fiL1jh4YJ3BbpPx3IGU",
        "authDomain": "bdat-web-app.firebaseapp.com",
        "databaseURL": "https://bdat-web-app.firebaseio.com",
        "storageBucket": "bdat-web-app.appspot.com",
        "projectId": "bdat-web-app",
        "messagingSenderId": "466614626356",
        "appId": "1:466614626356:web:5ab21f73bad8afa0538261",
        "measurementId": "G-Q91NYNGXJR"
    }

    def __init__(self):
        self.firebase = pyrebase.initialize_app(FirebaseClient.firebaseConfig)

    def getDatabase(self):
        return self.firebase.database()
