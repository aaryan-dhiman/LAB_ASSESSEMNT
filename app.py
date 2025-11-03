from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello — lab Assessment Flask app running!"

@app.route('/add', methods=['POST'])
def add():
    data = request.get_json() or {}
    a = data.get('a', 0)
    b = data.get('b', 0)
    try:
        result = a + b
    except Exception:
        return jsonify({"error": "a and b must be numbers"}), 400
    return jsonify({"sum": result})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
