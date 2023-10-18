from chat_app import socketio
from flask_socketio import send, emit
from flask import request

# Use Redis when needed 
User = {}

@socketio.on("connect")
def handle_connect():
    print("hello mot ngay that dep nha")

@socketio.on("user_join")
def handle_user_join(username):
    User[request.sid] = username
    message = f"{username} has entered chat"
    emit("announcement", message, broadcast=True)

@socketio.on("message")
def handle_message(message):
    username = User[request.sid]
    emit("new_message",{"username": username, "message": message}, broadcast=True)