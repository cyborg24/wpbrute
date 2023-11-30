import pyrebase

config = {
"apiKey": "AIzaSyAn-aVDj9zf0BLm59NAdPGXZC43n3vvfCc",
"authDomain": "kudi-ai.firebaseapp.com",
"databaseURL": "https://business-banking-93cc1-default-rtdb.firebaseio.com",
"projectId": "business-banking-93cc1",
"storageBucket": "business-banking-93cc1.appspot.com",
"messagingSenderId": "374159656381",
"appId": "1:374159656381:web:46ded5449543474131fed4",
"measurementId": "G-MG8RQTWYWF"
}

firebase = pyrebase.initialize_app(config)

#print(firebase.get)
database = firebase.database()

data = database.child().get()
print(data.val())
"""
for result in data.each():
    print(result.val())
"""