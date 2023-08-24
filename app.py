from flask import Flask, render_template
from flask_socketio import SocketIO, emit
import json

app = Flask(__name__)
socketio = SocketIO(app)

# Store drawing data temporarily (in-memory) - replace with a database for a production app
drawings = {}

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('draw')
def draw(data):
    drawings[data['id']].append(data)
    emit('drawing', data, broadcast=True)

@socketio.on('start_drawing')
def start_drawing(data):
    drawings[data['id']].append(data)


@socketio.on('stop_drawing')
def stop_drawing(data):
    drawings[data['id']].append('stop')
    emit('stop_drawing', data, broadcast=True)
    print(str(drawings))


@socketio.on('client_connected')
def client_connected(data):
    client_id = data['id']
    add_client(client_id=client_id)


@socketio.on('clear')
def clear():
    clear_drawing_data()  # Clear the drawings list
    emit('cleared', broadcast=True)

@app.route('/get_drawings')
def get_drawings():
    return json.dumps({'drawings': drawings})


def add_client(client_id):
    drawings[client_id] = []


def clear_drawing_data():
    for id in drawings:
        drawings[id].clear()



if __name__ == '__main__':
    socketio.run(app, debug=True)
