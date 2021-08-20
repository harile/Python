import requests
from win10toast import ToastNotifier
import json
import time

def update():
     r = requests.get('https://coronavirus-19-api.herokuapp.com/all')
     data = r.json()
     text =  f'Coronavirus cases:\t{data["cases"]}\nDeaths:\t{data["deaths"]}\nRecovered:\t{data["recovered"]}'

     while True:
         t =  ToastNotifier()
         t.show_toast("Covid19 Update", text, duration = 20)
         time.sleep(60)
        #  Them ghi chu

update()

