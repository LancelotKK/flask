from flask import Flask, request, jsonify, render_template
from datetime import datetime
import json

app = Flask(__name__)

# 用于存储历史数据
data_storage = []

# 接收 PyQt 发送的数据的端点
@app.route('/data', methods=['POST'])
def receive_data():
    data = request.json  # 获取 JSON 格式的数据
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # 当前时间
    record = {
        "time": timestamp,
        "aluminum": data.get("aluminum"),
        "iron": data.get("iron"),
        "silicon": data.get("silicon")
    }
    data_storage.append(record)  # 添加到历史记录
    print("Received data:", record)
    return jsonify({"status": "success", "data": record})

# 获取所有数据记录的端点
@app.route('/get_data', methods=['GET'])
def get_data():
    return jsonify(data_storage)

# 显示网页的端点
@app.route('/')
def index():
    return render_template('index.html')

# if __name__ == '__main__':
#     app.run(debug=True, port=5000)
if __name__ == '__main__':
    app.run(debug=True)
