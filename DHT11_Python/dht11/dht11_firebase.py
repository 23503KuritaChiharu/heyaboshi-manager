import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

import RPi.GPIO as GPIO
import dht11
import time
import datetime


# initialize GPIO
GPIO.setwarnings(True)
GPIO.setmode(GPIO.BCM)

# read data using pin 14
instance = dht11.DHT11(pin=14)

try:
    while True:
        result = instance.read()
        if result.is_valid():
            print("Last valid input: " + str(datetime.datetime.now()))

            print("Temperature: %-3.1f C" % result.temperature)
            print("Humidity: %-3.1f %%" % result.humidity)

        time.sleep(30)

except KeyboardInterrupt:
    print("Cleanup")
    GPIO.cleanup()


# cred = credentials.Certificate('./<your service account json>')
cred = credentials.Certificate('/home/pi/Desktop/heyaboshi-manager/DHT11_Python/heyaboshi-manager-firebase-adminsdk-avq9f-8e91ef2815.json')

firebase_admin.initialize_app(cred, {
    # 'databaseURL': 'https://<your database url>'
    'databaseURL': 'https://heyaboshi-manager.firebaseio.com/',
    'databaseAuthVariableOverride': {
        'uid': 'my-service-worker'
    }
})

##databaseに初期データを追加する
users_ref = db.reference('/devices/test_device_1')

# users_ref.set({
#     'user001': {
#         'date_of_birth': 'June 23, 1984',
#         'full_name': 'Sazae Isono'
#         },
#     'user002': {
#         'date_of_birth': 'December 9, 1995',
#         'full_name': 'Tama Isono'
#         }
#     })

# databaseにデータを追加する
users_ref.child('3').set({
        'humidity': result.humidity, 
        'tempareture': result.temperature,
        'time' : str(datetime.datetime.now()),
        'water_content': 0.2
})

users_ref.child('4').set({
        'humidity': 38, 
        'tempareture': 11,
        'time' : '2020-08-28 10:50:44',
        'water_content': 0.2
})

##データを取得する
print(users_ref.get())


