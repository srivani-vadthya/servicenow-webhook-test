from flask import Flask, request, jsonify
import datetime

app = Flask(__name__)

@app.route("/")
def home():
    return {
        "message": "ServiceNow Webhook Server Running"
    }

@app.route("/incident", methods=["POST"])
def incident():

    data = request.json

    print("\n")
    print("===================================")
    print("SERVICENOW INCIDENT RECEIVED")
    print("===================================")

    print(f"Time: {datetime.datetime.now()}")
    print(data)

    response = {
        "status": "success",
        "message": "Incident received",
        "incident": data.get("incident"),
        "triggered": True
    }

    return jsonify(response), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)