from flask import Flask, render_template
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

port = int(os.environ.get("PORT", 5000))

@app.route("/")
def home():
    return render_template("dechets_webcam.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=port)

