from flask import Flask, send_from_directory
from flask_cors import CORS
import os
port = int(os.environ.get("PORT", 5000))
app.run(host="0.0.0.0", port=port)

app = Flask(__name__, static_folder=".")
CORS(app)  # Active CORS sur toutes les routes

@app.route("/")
def serve_index():
    return send_from_directory(".", "dechets_webcam.html")  

@app.route("/<path:filename>")
def serve_file(filename):
    return send_from_directory(".", filename)

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
