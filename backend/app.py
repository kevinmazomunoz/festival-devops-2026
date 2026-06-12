from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  

@app.route("/api/festival")
def festival():
    return jsonify({
        "nombre": "Pacific DevOps Music Fest",
        "fecha": "2026-08-15",
        "artistas": [
            "DJ Docker",
            "Flask Beats",
            "Kubernetes Live"
        ],
        "estado": "Activo"
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)