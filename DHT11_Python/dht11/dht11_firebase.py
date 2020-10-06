import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

import RPi.GPIO as GPIO
import dht11
import time
import datetime

def db():
    # cred = credentials.Certificate('./<your service account json>')
    cred = credentials.Certificate('/home/pi/Desktop/heyaboshi-manager/DHT11_Python/heyaboshi-manager-firebase-adminsdk-815.json')

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
            'humidity': 38, 
            'tempareture': 11,
            'time' : '2020-08-28 10:30:44',
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

def main():
    db()

if __name__ == '__main__':
    main()
