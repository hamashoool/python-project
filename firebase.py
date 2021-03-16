import pyrebase


firebaseConfig = {
    "apiKey": "AIzaSyCfmF9Htjqaru1IjLSeajeYAV4sjf-z_BA",
    "authDomain": "rescue-e7eb6.firebaseapp.com",
    "databaseURL": "https://rescue-e7eb6-default-rtdb.firebaseio.com",
    "projectId": "rescue-e7eb6",
    "storageBucket": "rescue-e7eb6.appspot.com",
    "messagingSenderId": "658437640948",
    "appId": "1:658437640948:web:f9fa4cda1abfb4a59d84a1",
    "measurementId": "G-SXLSS5VNDV"
}

firebase_ = pyrebase.initialize_app(firebaseConfig)

auth = firebase_.auth()
#
email = input("email: ")
pss = input("pass: ")

user = auth.sign_in_with_email_and_password(email, pss)
print(auth.get_account_info(user['idToken']))

# print(f.FirebaseApplication('https://rescue-e7eb6-default-rtdb.firebaseio.com/', None))