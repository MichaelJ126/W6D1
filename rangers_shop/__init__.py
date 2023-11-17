from flask import Flask
from config import Config 

app = Flask(__name__)

app.config.from_object(Config)
@app.route("/")
def send_help():
    return "<p>Send Help!</p>"