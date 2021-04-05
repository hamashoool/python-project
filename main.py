import datetime
import json
import os
import threading

import geocoder as geocoder
import plyer

import firebase_admin as f
from firebase_admin import firestore
import pyrebase
from firebase_admin import credentials, auth as a
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.metrics import dp
from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.datatables import MDDataTable
from kivymd.uix.dialog import MDDialog
from kivymd.uix.list import OneLineAvatarIconListItem, ILeftBodyTouch, TwoLineIconListItem, \
    IconLeftWidget
from kivymd.uix.selectioncontrol import MDCheckbox

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
db = firestore.client()

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


class ListItemWithCheckbox(OneLineAvatarIconListItem):
    pass


class LeftCheckbox(ILeftBodyTouch, MDCheckbox):
    pass


class RescueGirlsApp(MDApp):
    user_ref = db.collection('Users')
    dialog = None
    dialog2 = None
    search_error = None
    search_repeat = None
    not_savior = None
    saviors_full = None
    reg_name_check = None
    data = {}
    text = ""
    previous_search = []

    def build(self):
        self.theme_cls.primary_palette = "Red"
        self.theme_cls.primary_hue = "700"
        self.theme_cls.theme_style = "Light"
        return Builder.load_file('main.kv')

    # this is the function that will check the database automatically every 10 seconds.
    def hello(self, *args):
        self.text += "."
        print(f"{self.text}")

    def on_start(self):
        # plyer.notification.notify(title='Tusaale', message="Notification using plyer", app_name='Rescue Girls',
        #                           app_icon='img/1.ico', timeout=10)  # this is the notification
        # Clock.schedule_interval(self.hello, 5) # here is where I call the function

        # Check login.txt file if it exist if it exist use the recorded info and login
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
            result = db.collection('Users').document(email).get()

            if result.to_dict()['user_type'] == 'Female':
                self.root.ids.person_name.text = result.to_dict()['name']
                self.root.ids.person_email.text = email
                self.root.current = 's3'
            else:
                self.root.ids.person_name_1.text = result.to_dict()['name']
                self.root.ids.person_email_1.text = email
                self.root.current = 's4'

                # getting alerts of the savior
                alerts = db.collection('Users').document(email).collection('Alerts').order_by(u'date_time',
                                                                                              direction=firestore.Query.DESCENDING).get()
                for alert in alerts:
                    lat = alert.to_dict()['latitude']
                    long = alert.to_dict()['longitude']
                    alert_list_view = self.root.ids.savior_alerts_list
                    alert_icon = IconLeftWidget(icon="alert",
                                                theme_text_color="Custom",
                                                text_color=(0, 208 / 255.0, 1, 1))
                    alert_items = TwoLineIconListItem(text=alert.to_dict()['name'],
                                                      secondary_text=f'{lat} , {long}',
                                                      pos_hint={"center_x": .1, "center_y": .7})
                    alert_items.add_widget(alert_icon)
                    alert_list_view.add_widget(alert_items)

                # Create an Event for notifying main thread.
                callback_done = threading.Event()

                # Create a callback on_snapshot function to capture changes
                def on_snapshot(doc_snapshot, changes, read_time):
                    current_alerts = []
                    for doc in doc_snapshot:
                        current_alerts.append(doc.id)
                    last_one = current_alerts[-1]
                    plyer.notification.notify(title='Rescue Girl', message="Notification using plyer",
                                              app_name='Rescue Girls',
                                              app_icon='img/1.ico', timeout=10)  # this is the notification
                    self.savior_alert_refresh()
                    print(f'{last_one}')
                    callback_done.set()

                doc_ref = db.collection('Users').document(email).collection('Alerts').order_by(u'date_time',
                                                                                               direction=firestore.Query.DESCENDING)

                # Watch the document
                doc_watch = doc_ref.on_snapshot(on_snapshot)

    def login(self):
        email = self.root.ids.email_login.text
        password = self.root.ids.password_login.text
        try:
            user_ = a.get_user_by_email(email)
        except:
            pass
        try:

            # login using pyrebase module
            user = auth.sign_in_with_email_and_password(email=email, password=password)

            info = self.user_ref.document(email).get()
            name = info.to_dict()['name']
            user_type = info.to_dict()['user_type']
            self.data['user'] = []
            self.data['user'].append({
                'email': email,
                'pass': password,
                'uid': user_.uid,
                'name': name,
                'user_type': user_type,
            })

            if user_type == 'Female':
                self.root.current = 's3'
            else:
                self.root.current = 's4'

            # create login.txt and save the user's info
            with open('login.txt', 'w') as file:
                json.dump(self.data, file)
            self.root.ids.email_login.text = ""
            self.root.ids.password_login.text = ""

        except:
            if not self.dialog:
                self.dialog = MDDialog(
                    text="Invalid email or password.",
                )
            self.dialog.open()

    def registration(self):
        email = self.root.ids.email_reg.text
        password = self.root.ids.password_reg.text
        name = self.root.ids.name_reg.text

        if name == "":
            if not self.reg_name_check:
                self.reg_name_check = MDDialog(
                    text="You must enter your full name.",
                )
            self.reg_name_check.open()
        else:
            try:

                # create user using pyrebase module
                auth.create_user_with_email_and_password(email=email, password=password)
                auth.sign_in_with_email_and_password(email=email, password=password)

                try:
                    user_ = a.get_user_by_email(email)
                except:
                    pass

                person = ""

                # checking the user type
                if self.root.ids.female_check.active:
                    person = "Female"
                elif self.root.ids.savior_check.active:
                    person = "Savior"

                # save the user info to firestore 'user_ref' which is firestore.client()
                self.user_ref.document(user_.email).set({
                    'name': name,
                    'email': email,
                    'password': password,
                    'id': user_.uid,
                    'user_type': person

                })

                # redirect to the home page after the registration
                if person == 'Female':
                    self.root.current = 's3'
                else:
                    self.root.current = 's4'

                # save the user date in the login.txt file
                self.data['user'] = []
                self.data['user'].append({
                    'email': email,
                    'pass': password,
                    'uid': user_.uid,
                    'name': name,
                    'user_type': person
                })
                with open('login.txt', 'w') as file:
                    json.dump(self.data, file)

                # clear the from after registration
                self.root.ids.email_reg.text = ""
                self.root.ids.password_reg.text = ""
                self.root.ids.name_reg.text = ""
            except:
                if not self.dialog2:
                    self.dialog2 = MDDialog(
                        text="Invalid registration info.",
                    )
                self.dialog2.open()

    def logout(self):
        os.remove("login.txt")
        self.root.current = 'login'

    def search_savior(self, search=False):
        if search:

            # get the text from the input
            savior = self.root.ids.savior_search.text

            # initiate the database location using firebase_admin
            result = db.collection('Users').document(savior).get()

            # get the user if the user exists and not the previously searched and user type is saviour
            if result.exists and savior not in self.previous_search:
                if result.to_dict()['user_type'] == 'Savior':
                    self.previous_search.append(savior)
                    list_view = self.root.ids.search_result_list
                    icon = IconLeftWidget(icon="account-plus", on_release=self.add_savior)
                    items = TwoLineIconListItem(text=result.to_dict()['name'],
                                                secondary_text=result.to_dict()['email'],
                                                pos_hint={"center_x": .1, "center_y": .7})
                    items.add_widget(icon)
                    list_view.add_widget(items)
                else:
                    if not self.not_savior:
                        self.not_savior = MDDialog(
                            text="This user is not a savior.",
                        )
                    self.not_savior.open()
            elif savior in self.previous_search:
                if not self.search_repeat:
                    self.search_repeat = MDDialog(
                        text="User already found.",
                    )
                self.search_repeat.open()
            else:
                if not self.search_error:
                    self.search_error = MDDialog(
                        text="Invalid Email.",
                    )
                self.search_error.open()

    def add_savior(self, *args):

        # getting current user
        user_email = ""
        if os.path.isfile('login.txt'):
            with open('login.txt') as json_file:
                data = json.load(json_file)
                for p in data['user']:
                    if p['email'] == "":
                        pass
                    else:
                        user_email = p['email']
        if user_email == "":
            pass
        else:

            # getting the input form the user and checking if the user exists and not previously searched
            savior = self.root.ids.savior_search.text
            if savior in self.previous_search:

                # getting the total saved saviors of the user or the 'girl' and check if they reach the maximum.
                saviors = self.user_ref.document(user_email).collection('Saviors').get()
                if len(saviors) <= 4:

                    # getting the savior info and save it to the girl's Savior collection
                    result = db.collection('Users').document(savior).get()
                    self.user_ref.document(user_email).collection('Saviors').document(savior).set({
                        'name': result.to_dict()['name'],
                        'email': result.to_dict()['email']
                    })
                else:
                    if not self.saviors_full:
                        self.saviors_full = MDDialog(
                            text="You have reached the maximum contact list.",
                        )
                    self.saviors_full.open()

    # clear the search list view
    def clear_list(self):
        items = self.root.ids.search_result_list
        list_item = self.root.ids.search_result_list.children
        while list_item:
            for itm in list_item:
                items.remove_widget(itm)
        self.previous_search.clear()
        self.root.ids.savior_search.text = ""

    # rescue me button function
    def rescue_me(self):

        # getting current location of the user or the 'girl'
        location = geocoder.ip('me')
        latitude = location.lat
        longitude = location.lng

        # getting current user
        user_email = ""
        user_name = ""
        if os.path.isfile('login.txt'):
            with open('login.txt') as json_file:
                data = json.load(json_file)
                for p in data['user']:
                    if p['email'] == "":
                        pass
                    else:
                        user_email = p['email']
                        user_name = p['name']
        if user_email == "" and user_name == "":  # make sure registration require name
            pass
        else:
            # getting the saved saviors of this user or 'girl'
            saviors = self.user_ref.document(user_email).collection('Saviors').get()

            # send her location, name and time to each of them
            for savior in saviors:
                data = {
                    'email': user_email,
                    'name': user_name,
                    'latitude': latitude,
                    'longitude': longitude,
                    'date_time': datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                }
                self.user_ref.document(savior.to_dict()['email']).collection('Alerts').add(data)

    def savior_alert_refresh(self):

        # get the logged in user info
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
            # clear previous alert list
            items = self.root.ids.savior_alerts_list
            list_item = self.root.ids.savior_alerts_list.children
            while list_item:
                for itm in list_item:
                    items.remove_widget(itm)

            # get the new alert list
            alerts = db.collection('Users').document(email).collection('Alerts').order_by(u'date_time',
                                                                                          direction=firestore.Query.DESCENDING).get()
            for alert in alerts:
                lat = alert.to_dict()['latitude']
                long = alert.to_dict()['longitude']
                date_time = alert.to_dict()['date_time']
                alert_list_view = self.root.ids.savior_alerts_list
                alert_icon = IconLeftWidget(icon="alert",
                                            theme_text_color="Custom",
                                            text_color=(0, 208 / 255.0, 1, 1))
                alert_items = TwoLineIconListItem(text=alert.to_dict()['name'],
                                                  secondary_text=f'{date_time}',
                                                  pos_hint={"center_x": .1, "center_y": .7})
                alert_items.add_widget(alert_icon)
                alert_list_view.add_widget(alert_items)

    def alert_listener(self):
        print('Alert')

    def printt(self, *args):
        print('Added')


RescueGirlsApp().run()
