from flask import Flask, jsonify
from flask_cors import CORS
import time

app = Flask(__name__)
CORS(app)  # allow browser requests from your frontend

# sample endpoint -- return list of locations
@app.route('/locations', methods=['GET'])
def locations():
    # Example: return empty list or some test points
    data = [
        # Example record format expected by the frontend
        {"studentId":"STU001","lat":12.9716,"lng":77.5946,"timestamp":int(time.time()), "studentName":"Aarav Sharma"}
    ]
    return jsonify(data)

# optionally expose root to avoid "Not Found" when browsing /
@app.route('/', methods=['GET'])
def index():
    return "Flask server running. Use /locations for JSON."

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
