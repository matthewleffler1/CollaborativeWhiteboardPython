from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)
socketio = SocketIO(app)

# Store drawing data temporarily (in-memory) - replace with a database for a production app
drawings = []

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('draw')
def draw(data):
    drawings.append(data)
    emit('drawing', data, broadcast=True)

@socketio.on('clear')
def clear():
    drawings.clear()  # Clear the drawings list
    emit('cleared', broadcast=True)

@app.route('/get_drawings')
def get_drawings():
    return {'drawings': drawings}

if __name__ == '__main__':
    socketio.run(app, debug=True)
