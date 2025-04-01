import gevent.monkey
gevent.monkey.patch_all()  # ✅ Patch all before imports


from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_socketio import SocketIO, emit
from groq import prompts,send_request_json,generateType_json
# from test import gemini_request

app = Flask(__name__)
CORS(app)
# ✅ Explicitly set WebSocket mode to "gevent_uwsgi"
socketio = SocketIO(app,  cors_allowed_origins="*")

@socketio.on("connect")
def handle_connect():
    print("Client connected")
    emit("server_message", {"message": "Connected to WebSocket!"})

@socketio.on("disconnect")
def handle_disconnect():
    print("Client disconnected")

@socketio.on("send_message")
def handle_message(data):
    print(f"Received WebSocket message: {data}")
    content = generateType_json(data)
    print(content)
    emit("server_response", {"message":content}, broadcast=True)


@app.route('/', methods=['POST'])
def home():
    req = request.json
    hintType = req["hintType"]
    hintContent = req["hintContent"]
    content = prompts(hintType,hintContent)
    print(req)
    
    return content if content else " "


if __name__ == "__main__":
    socketio.run(app)