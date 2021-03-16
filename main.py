import json
import os
import plyer

import firebase_admin as f
import pyrebase
from firebase_admin import credentials, auth as a
from kivy.clock import Clock
from kivy.core.window import Window
from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.dialog import MDDialog

Window.size = (300, 500)  # remove before production

app = {
  "type": "service_account",
  "project_id": "rescue-e7eb6",
  "private_key_id": "7147cbc103bf82a150599b9a23f5df7d81e4d070",
  "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvAIBADANBgkqhkiG9w0BAQEFAASCBKYwggSiAgEAAoIBAQDFtaHxB8PaLqk1\nWX3qWiX3F0gbDwT1sGK6B4V/3pbO6CTWOXHS45dIMJXHK8mwnMpC7nw0UdSrsihu\nVh6Z3O1WNTJPvlDKFmCUVIOKAkfjaJKjB+9bCrlyA3ICgDfeN2vFgbsr+Gd1Bi3P\nK3t+5/lwBxMuacWjempJucj9Bx4olyBw/jrt/Jy2y1XGKK0ZK/Bd5VI9XzQ56/9I\nXnr+ysjPxrauGcoKCfM8rc5RfigR9t0c3SC9yTZRvXOgcQTgJ2dv9RZ5lchuOF2q\nhk7nwy7dEfGAQ7AcCvt5GP1bJC55/C/uLoFT/LKoFDrj3Ok4WXWomKN8M+raiu9P\n+T4YsP8ZAgMBAAECggEAU+MYPiu8RvPraa56BZiQaUHgn1KFGTXo/eO5GiM4u7u1\n/YtMJ13Xz5KFyodiwWQVUcbcvlpGMT+bdg1mWIRr01so6LrojoZmHimp0kHbfLrf\nFPuF7IwlWSHrGvKKQegj+x5ra2Gvi/C+ORvK/3Kv3H+z/Mp2SEHlnTiN9gYyHqgZ\n+qmD9rK9jfZYJLgjctTl2or4zzGtn7QBjFx11xjKfE8tssm3tLNuVIyCzFWYWlkQ\nmtm1bWIEe8ClRH1ROr437PbEGPcb18bR31URxMBx/1O6tOmjgebGzZEFWmXMf4m9\nkRHpn7uuEOLQagQb5+7+ttstyp2onpmDWfRJlG8vTQKBgQDhTDmc3n17oV2/xh21\nbHTT2/xL0KUN476i+6hKfLY3Vzy/VnVbEj0mBfZcPXqvdUjZaD8pJd13ePUMGaqy\nis5rY8MdLDiLZ+RzsziVxu22l6ybjUcQY68vfnazbEL+n/pI7C4rNfoo8aPjSs7f\nXJLr8lc/QdLt7HOm4bo0QUYOnwKBgQDgpvWNbDmvBSuvqFdEk0ZpGZX9dydGHQJm\nzPlWp2pUM7AgVETbsNFsQyDPBsyDJ154685YAqVFuwuVK42apf//1sYX+ukaPDAW\nEBjEezXVqXru9h97/qMQywea470UqYizRSN4c2oCcsFPF8GsP5BOiP0tDBqRFbts\nOs3/lpRvRwKBgHbBiCjQ+lHdiB4bHvPPnHFEJuQLscT1hDpC7r18qUvYdxPgTfHY\nVlUhlW+flHjCGMlIcuqMpAViw8BCE0ETe6UNq/5HnfKVq8z07mG8vvadUoWX3Zqd\nAO3G+mivK00uJG6l19w9EoTcgme/ufXwxR0L28NjPfzdw0R2/YCn23a/AoGAeRfF\n+ItDtKG24KJ/F8nDBFf0T4Hwu4xbhQorxJfNasHJyENkMn9nA1JT1wQ1LOUFuWxx\n92LFr4aZQbkORTQBf+hHMxnemHOk/9+BWjeH1znZuAEXC4FAaIbn/IeRnhecRfWY\nnw6nL9aneHi3vp8srAiPX77MezQZqMcxzvld3XUCgYAaqv0ufJ9hTeD/KfIdHTQG\nF5iMGNpWCr5BOF3QK4IKPn0sVwS3BLbe0dRJlwXZr/YNyFsEjvjwVqQzuckqhMF7\nrGoxsZipqKkhfMUt4zM1qNCVg66YhMWnAHhmsCBY4gMj35cOc0PGSc7LvIKdqf1q\n2YnRENFpftpWtvzKt4V5IQ==\n-----END PRIVATE KEY-----\n",
  "client_email": "firebase-adminsdk-jxk79@rescue-e7eb6.iam.gserviceaccount.com",
  "client_id": "107353584054383964563",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-jxk79%40rescue-e7eb6.iam.gserviceaccount.com"
}

cred = credentials.Certificate(app)

f.initialize_app(cred,{
  'databaseURL': 'https://rescue-e7eb6-default-rtdb.firebaseio.com/'
})

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


class MainApp(MDApp):
    dialog = None
    data = {}
    text = ""

    # this is the function that will check the database automatically every 10 seconds.
    def hello(self, *args):
        self.text += "."
        print(f"{self.text}")

    def on_start(self):
        # plyer.notification.notify(title='Tusaale', message="Notification using plyer", app_name='Rescue Girls',
        #                           app_icon='img/1.ico', timeout=10)  # this is the notification
        # Clock.schedule_interval(self.hello, 5) # here is where I call the function
        email = ""
        password = ""
        if os.path.isfile('login.txt'):
            with open('login.txt') as json_file:
                data = json.load(json_file)
                for p in data['user']:
                    if p['email'] == "" or p['pass'] == "":
                        pass
                    else:
                        email = p['email']
                        password = p['pass']
        if email == "" or password == "":
            pass
        else:
            user = auth.sign_in_with_email_and_password(email=email, password=password)
            self.root.current = 's3'

    def build(self):
        self.theme_cls.primary_palette = "Red"
        self.theme_cls.primary_hue = "700"
        self.theme_cls.theme_style = "Light"
        return Builder.load_file('main.kv')

    def login(self):
        email = self.root.ids.email_login.text
        password = self.root.ids.password_login.text
        user_ = a.get_user_by_email(email)
        try:
            user = auth.sign_in_with_email_and_password(email=email, password=password)
            self.root.current = 's3'
            self.root.ids.welcome.text = "Hey! your email is %s " % email
            self.data['user'] = []
            self.data['user'].append({
                'email': email,
                'pass': password,
                'uid': user_.uid
            })
            with open('login.txt', 'w') as file:
                json.dump(self.data, file)
        except:
            if not self.dialog:
                self.dialog = MDDialog(
                    text="Invalid email or password.",
                )
            self.dialog.open()


MainApp().run()
