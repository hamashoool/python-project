import firebase_admin
from firebase_admin import credentials, db
from firebase_admin import auth
from firebase_admin._auth_utils import EmailAlreadyExistsError

# app = {
#   "type": "service_account",
#   "project_id": "rescue-e7eb6",
#   "private_key_id": "7147cbc103bf82a150599b9a23f5df7d81e4d070",
#   "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvAIBADANBgkqhkiG9w0BAQEFAASCBKYwggSiAgEAAoIBAQDFtaHxB8PaLqk1\nWX3qWiX3F0gbDwT1sGK6B4V/3pbO6CTWOXHS45dIMJXHK8mwnMpC7nw0UdSrsihu\nVh6Z3O1WNTJPvlDKFmCUVIOKAkfjaJKjB+9bCrlyA3ICgDfeN2vFgbsr+Gd1Bi3P\nK3t+5/lwBxMuacWjempJucj9Bx4olyBw/jrt/Jy2y1XGKK0ZK/Bd5VI9XzQ56/9I\nXnr+ysjPxrauGcoKCfM8rc5RfigR9t0c3SC9yTZRvXOgcQTgJ2dv9RZ5lchuOF2q\nhk7nwy7dEfGAQ7AcCvt5GP1bJC55/C/uLoFT/LKoFDrj3Ok4WXWomKN8M+raiu9P\n+T4YsP8ZAgMBAAECggEAU+MYPiu8RvPraa56BZiQaUHgn1KFGTXo/eO5GiM4u7u1\n/YtMJ13Xz5KFyodiwWQVUcbcvlpGMT+bdg1mWIRr01so6LrojoZmHimp0kHbfLrf\nFPuF7IwlWSHrGvKKQegj+x5ra2Gvi/C+ORvK/3Kv3H+z/Mp2SEHlnTiN9gYyHqgZ\n+qmD9rK9jfZYJLgjctTl2or4zzGtn7QBjFx11xjKfE8tssm3tLNuVIyCzFWYWlkQ\nmtm1bWIEe8ClRH1ROr437PbEGPcb18bR31URxMBx/1O6tOmjgebGzZEFWmXMf4m9\nkRHpn7uuEOLQagQb5+7+ttstyp2onpmDWfRJlG8vTQKBgQDhTDmc3n17oV2/xh21\nbHTT2/xL0KUN476i+6hKfLY3Vzy/VnVbEj0mBfZcPXqvdUjZaD8pJd13ePUMGaqy\nis5rY8MdLDiLZ+RzsziVxu22l6ybjUcQY68vfnazbEL+n/pI7C4rNfoo8aPjSs7f\nXJLr8lc/QdLt7HOm4bo0QUYOnwKBgQDgpvWNbDmvBSuvqFdEk0ZpGZX9dydGHQJm\nzPlWp2pUM7AgVETbsNFsQyDPBsyDJ154685YAqVFuwuVK42apf//1sYX+ukaPDAW\nEBjEezXVqXru9h97/qMQywea470UqYizRSN4c2oCcsFPF8GsP5BOiP0tDBqRFbts\nOs3/lpRvRwKBgHbBiCjQ+lHdiB4bHvPPnHFEJuQLscT1hDpC7r18qUvYdxPgTfHY\nVlUhlW+flHjCGMlIcuqMpAViw8BCE0ETe6UNq/5HnfKVq8z07mG8vvadUoWX3Zqd\nAO3G+mivK00uJG6l19w9EoTcgme/ufXwxR0L28NjPfzdw0R2/YCn23a/AoGAeRfF\n+ItDtKG24KJ/F8nDBFf0T4Hwu4xbhQorxJfNasHJyENkMn9nA1JT1wQ1LOUFuWxx\n92LFr4aZQbkORTQBf+hHMxnemHOk/9+BWjeH1znZuAEXC4FAaIbn/IeRnhecRfWY\nnw6nL9aneHi3vp8srAiPX77MezQZqMcxzvld3XUCgYAaqv0ufJ9hTeD/KfIdHTQG\nF5iMGNpWCr5BOF3QK4IKPn0sVwS3BLbe0dRJlwXZr/YNyFsEjvjwVqQzuckqhMF7\nrGoxsZipqKkhfMUt4zM1qNCVg66YhMWnAHhmsCBY4gMj35cOc0PGSc7LvIKdqf1q\n2YnRENFpftpWtvzKt4V5IQ==\n-----END PRIVATE KEY-----\n",
#   "client_email": "firebase-adminsdk-jxk79@rescue-e7eb6.iam.gserviceaccount.com",
#   "client_id": "107353584054383964563",
#   "auth_uri": "https://accounts.google.com/o/oauth2/auth",
#   "token_uri": "https://oauth2.googleapis.com/token",
#   "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
#   "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-jxk79%40rescue-e7eb6.iam.gserviceaccount.com"
# }
#
# cred = credentials.Certificate(app)
#
# firebase_admin.initialize_app(cred,{
#   'databaseURL': 'https://rescue-e7eb6-default-rtdb.firebaseio.com/'
# })
#
# user = firebase_admin.auth.get_user_by_email('osmanjack12@gmail.com')
# print(user.uid)


# email = input("Enter Email: ")
# passw = input("Enter Password: ")
#
# ext = ['@gmail.com', '@hotmail.com', '@yahoo.com']
# e_check = False
# p_check = False
# try:
#     for com in ext:
#         if com in email:
#             e_check = True
#     if not e_check:
#         print("Your email must contain '@gmail.com', '@hotmail.com' or '@yahoo.com'.")
#     if len(passw) < 6:
#         print('your password must contain 6 or more characters.')
#     else:
#         p_check = True
#     if e_check and p_check:
#         user = auth.create_user(email=email, password=passw)
#         print(user)
# except EmailAlreadyExistsError:
#     print('user exist')

