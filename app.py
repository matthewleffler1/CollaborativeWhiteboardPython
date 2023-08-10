from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Store drawing data temporarily (in-memory) - replace with a database for a production app
drawings = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/draw', methods=['POST'])
def draw():
    data = request.json
    drawings.append(data)
    return jsonify(success=True)

@app.route('/get_drawings', methods=['GET'])
def get_drawings():
    return jsonify(drawings)

if __name__ == '__main__':
    app.run(debug=True)
