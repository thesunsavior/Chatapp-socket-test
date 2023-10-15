from flask import Flask
from flask_socketio import SocketIO
from chat_app.config import Configuration

app = Flask(__name__)
app.config.from_object(Configuration)

socketio = SocketIO(app)

from chat_app import routes

if __name__ == "__main__":
    socketio.run(app)