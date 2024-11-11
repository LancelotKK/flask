import requests
import json

def send_data_to_server(al, fe, si):
    url = 'http://127.0.0.1:5000/data'  # Flask 服务器的 URL
    headers = {'Content-Type': 'application/json'}
    data = {
        "aluminum": al,
        "iron": fe,
        "silicon": si
    }  # 将三个测量值放入字典
    response = requests.post(url, data=json.dumps(data), headers=headers)
    print("Response from server:", response.json())
send_data_to_server(12.34, 56.78, 90.12)
