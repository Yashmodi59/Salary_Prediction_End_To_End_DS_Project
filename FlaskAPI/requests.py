from data_input import data_in
import requests as re
URL = 'http://127.0.0.1:5000/predict'
headers = {"Content-Type": "application/json"}
data = {"input": data_in}

r = re.get(URL,headers=headers, json=data)
print(r)
r.json()
