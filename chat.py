import requests
from datetime import datetime
import time
timestring = str(datetime.now)
url = "https://pythonavanzado.techtalents.cloud/chat/"
data = {"name": "armando"}


requests.post(url + "register", data) 



def send(message, name, url, time):
    if len(name) > 0 and len(name) < 20 and len(message) > 0 and len(message) < 200:
        data = {
            "name": name,
            "message": message,
            "time": time
        }
        result = requests.post(url, data = data)
        if not result.text == "Message sent.":
            print(result.text)

def recieve(url):
    recieved = requests.get(url)
    if recieved.status_code == 200:
        print(recieved.text)

while True:
    message = input()
    time = "{:02}:{:02}".format(datetime.now().hour, datetime.now().minute)       
    send(message, data["name"], url + "send", time)
    
    recieve(url + "messages")