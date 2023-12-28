from flask import Flask
import datetime

app = Flask(__name__)

@app.route("/")
def hello_world():
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")
    return f"<h1>Hello Flask!</h1><p>Current time is {current_time}</p>"
