import pyrebase

firebaseConfig = {
  "apiKey": "AIzaSyDsxvhMqXqatghcmteLHscZeEYVbu4x7rE",
  "authDomain": "prjcolegio-ab5ec.firebaseapp.com",
  "databaseURL": "https://prjcolegio-ab5ec-default-rtdb.firebaseio.com",
  "projectId": "prjcolegio-ab5ec",
  "storageBucket": "prjcolegio-ab5ec.appspot.com",
  "messagingSenderId": "690762303652",
  "appId": "1:690762303652:web:76c14e3c074f849ec9fe31",
  "measurementId": "G-PTSZSLRM09"
}

firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()

usuario = input('Ingrese usuario : ')
password = input('Ingrese su password : ')

try:
    usuario = auth.sign_in_with_email_and_password(usuario,password)
    data = auth.get_account_info(usuario['idToken'])
    print(data)
except:
    print('Datos incorrectos')
