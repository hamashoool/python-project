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
  "project_id": "rescue-girls",
  "private_key_id": "b3da2c900d27f6fb8a7426e0334db23bc499c801",
  "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQCvxpYPUPqOUihl\noaNLzfpZY0HMNMgFA+DILPEk1yqvjtjgQDmevYr+3gadr0XBauebwlXHG2DIuutb\nqgZNhuTrNYh0b7hyj4S5+JFC91lDgYz/73CX0h/7y17wj26/WKfGP5VsVuv1oJCJ\nQWOpliSyp/kdQJEvc4VqBrwPlQApCQ7iBHEmPE5VyMDP4jRdUEe1GHLxxB2maCTW\nfJkNlydcdROpG1MjrTFxtjNvZWPK5djMrirIAm5p4pV1d/aZbtT9r+mHs4BaFQy5\nMeXFHNGrV7ipaPVdUpJBqDb9kIu8oyWk+t4EL9wRNNQPNVKy4vfuT0XtM5sKFP2X\nI/bJm+BPAgMBAAECggEAOEAAMHmVHOtcwx1FYRJS7b0ORteTNMunaNe8+bGjltfL\nPoQ/DDYS33nUuyxmUb2wzY8UnSl9QO9UNxrDdpbW9hBFESHZcEvOSScq8TeviKNS\nKGsK6ILVOmI8CRaVdcVct1wMqMVuMEYISuwyhQgnyUZouXw6melJhgMOtpvTl82l\n8ynzQwZ5bvxCSpt5/u7XkLWeWg7MrQQXIRx7/nZehVSTTfKNG3FlIsZ/hFSs0aee\nYpT0dF9YMfcomW550aOSw7fLxshLOz0l3JVMhMFsBrCWPP3xvhgwdENKUvsBStz/\nwO+jGMNskCwXH1yZPnwP5qV8VaMTaMxuwv6DqvbrVQKBgQDwRxLx5np8r0/OOY1k\nUCK4QElFzd0ppETQT7fw0noNKe/OZeh5mDZh69Q2QP1secqnNoyMLC0inIw60xiP\nstnJS2i8pidrkWFo8CBIR3pwdP56ASMRfYYHqD1sQ+gml+oxpvr5EYoA1zvavEaL\nhu8fAL+jF/JJdeJ6JEfyD5UFkwKBgQC7RwgAJkqitGjt6e4ZpTSPkMWkcByBkzVj\nSzYjq12v2itG2uusWbXmFaSJwMJdhHpWIuE/k9J1D/ADp/GprkyuTRwySZzNynLe\n/wNn17sc2UExW3+M85e0hFC3w+nOYg/+9eI1M0+0jJJhkVXnK39FXhy01HgLt3z1\nvqh/xi7v1QKBgQDU6KXI48m1okK9IhI/ySJ60bwbtoc61uyDCaCcLGUqNPbhlTui\nQ1Ys/qNUT9I/xMvlz1hK/PohqUY4+cTR0FFbJQ7x2ukjT/dY3S493diIvaKgyVEh\ntnCFaHbE8IdNa1+CD8xj1z7J7+6BrEN2b2KDvk4RXq66mVLNmEiIHXaXMQKBgCLR\nGdOtSsLk930DuJhb9mGacKQZk7MjQxGqse3/tfMzhEgv+xCXvRGBhI13oKryLixF\nX8sKGF5bECwd1PfOx8K/4zYWKWi48pIyptdvbAH5Af3DHPt/bfzJfJgtfBI6eO7V\nl7B8UZ0nZS9ubaIEnCyxSnTz6z2CZ2DoiTr4BVHhAoGAAP5kCWCZwBW8KRNfqFMp\nbt9SdvnhldcFskKp+xTUuplIDC1zVH8JMgv1w/VZhhAJiaHggcmqZ4hQIxifnvLo\n26lgx1TM5hB7qR2/wEcQ4LB6w2vzg22gVVfhrVSK2laYaCacCeuqVodEDR7dG0om\nHKQzy0ckWmpiLEOOQMYWQd0=\n-----END PRIVATE KEY-----\n",
  "client_email": "firebase-adminsdk-pj0bx@rescue-girls.iam.gserviceaccount.com",
  "client_id": "112913675773140494875",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-pj0bx%40rescue-girls.iam.gserviceaccount.com"
}

cred = credentials.Certificate(app)

f.initialize_app(cred, {
  'databaseURL': 'https://rescue-girls-default-rtdb.firebaseio.com/'
})

firebaseConfig = {
    "apiKey": "AIzaSyA_NEfnRtKlhS5fkpNDB6qfvxU5-fmtBhQ",
    "authDomain": "rescue-girls.firebaseapp.com",
    "databaseURL": "https://rescue-girls-default-rtdb.firebaseio.com/",
    "projectId": "rescue-girls",
    "storageBucket": "rescue-girls.appspot.com",
    "messagingSenderId": "929788672406",
    "appId": "1:929788672406:web:2bf21fcac9d3da172545b7",
    "measurementId": "G-T2EP7MVTHR"
}

firebase_ = pyrebase.initialize_app(firebaseConfig)

auth = firebase_.auth()


class MainApp(MDApp):
    dialog = None
    dialog2 = None
    data = {}
    text = ""

    # this is the function that will check the database automatically every 10 seconds.
    def hello(self, *args):
        self.text += "."
        print(f"{self.text}")

    def on_start(self):
        plyer.notification.notify(title='Tusaale', message="Notification using plyer", app_name='Rescue Girls',
                                  app_icon='img/1.ico', timeout=10)  # this is the notification
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
            self.root.ids.welcome.text = "Welcome Back."

    def build(self):
        self.theme_cls.primary_palette = "Red"
        self.theme_cls.primary_hue = "700"
        self.theme_cls.theme_style = "Light"
        return Builder.load_file('main.kv')

    def login(self):
        email = self.root.ids.email_login.text
        password = self.root.ids.password_login.text
        try:
            user_ = a.get_user_by_email(email)
        except:
            pass
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

    def registration(self):
        email = self.root.ids.email_reg.text
        password = self.root.ids.password_reg.text
        try:
            user = auth.create_user_with_email_and_password(email=email, password=password)
            s_user = auth.sign_in_with_email_and_password(email=email, password=password)
            try:
                user_ = a.get_user_by_email(email)
            except:
                pass
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
            if not self.dialog2:
                self.dialog2 = MDDialog(
                    text="Invalid registration info.",
                )
            self.dialog2.open()


MainApp().run()
