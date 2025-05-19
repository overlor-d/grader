from flask import Flask, request, jsonify
import os, json
from datetime import datetime

app = Flask(__name__)
ARRIVAL_DIR = os.path.join("src", "grader_queue", "arrival")

@app.route("/submit", methods=["POST"])
def submit():
    data = request.get_json()
    if not data:
        return jsonify({"error": "Invalid JSON"}), 400

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S_%f")
    filename = f"submission_{timestamp}.json"
    filepath = os.path.join(ARRIVAL_DIR, filename)

    os.makedirs(ARRIVAL_DIR, exist_ok=True)
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)

    return jsonify({"status": "received", "filename": filename}), 200

def run_listener_api():
    app.run(host="0.0.0.0", port=5000, debug=False, use_reloader=False)
