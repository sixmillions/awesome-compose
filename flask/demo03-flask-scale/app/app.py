from flask import Flask
import time
import socket
from flask import jsonify

app = Flask(__name__)


@app.route("/")
def hello_world():
    hostname = socket.gethostname()
    # 获取本机ip
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    ip = s.getsockname()[0]
    return jsonify(
        {
            "success": True,
            "time": str(time.asctime(time.localtime(time.time()))),
            "msg": "ok",
            "data": {"ip": ip, "hostname": hostname},
        }
    )

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
