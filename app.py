from web_socket_server import WebSocketServer, socketio, app
from flask import render_template

app = WebSocketServer().create_app()

@socketio.on('connect')
def handle_connect():
    print('Client connected')

@socketio.on('disconnect')
def handle_disconnect():
    print('Client disconnected')

@socketio.on('message')
def handle_message(message):
    print(f'Received message: {message}')
    socketio.emit('message', message) #sends a message from us to the client

@app.route('/')
def index():
    return render_template('WebSocketClient.html')



if __name__ == '__main__':
    socketio.run(app)