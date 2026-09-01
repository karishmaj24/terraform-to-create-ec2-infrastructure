from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({
        "status": "success",
        "message": "CloudDeploy Backend is running"
    })

@app.route("/deploy")
def deploy():
    return jsonify({
        "status": "success",
        "message": "Deployment request received"
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
