from flask import Flask, request, jsonify
import os, json
from datetime import datetime
from werkzeug.serving import make_server

app = Flask(__name__)
ARRIVAL_DIR = os.path.join("src", "grader_queue", "arrival")

@app.route("/submit", methods=["POST"])
def submit():
    data = request.get_json()
    if not data:
        return jsonify({"error": "Invalid JSON"}), 400

    timestamp = datetime.now().strftime("%Y%m%d%H%M%S%f")
    filename = f"submission_{timestamp}.json"
    filepath = os.path.join(ARRIVAL_DIR, filename)

    os.makedirs(ARRIVAL_DIR, exist_ok=True)
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)

    return jsonify({"status": "received", "filename": filename}), 200

class FlaskServer:
    def __init__(self, host="0.0.0.0", port=5000):
        self.server = make_server(host, port, app)
        self.ctx = app.app_context()
        self.ctx.push()

    def run(self):
        self.server.serve_forever()

    def stop(self):
        self.server.shutdown()

server_instance = FlaskServer()

def run_listener_api():
    server_instance.run()
