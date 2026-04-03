from flask import Flask, jsonify, request

app = Flask(__name__)

members = []

@app.route("/")
def home():
    return jsonify({"message": "Welcome to ACEest Fitness API"})


@app.route("/members", methods=["GET"])
def get_members():
    return jsonify(members)


@app.route("/members", methods=["POST"])
def add_member():
    data = request.json

    member = {
        "name": data.get("name"),
        "program": data.get("program")
    }

    members.append(member)

    return jsonify(member), 201


@app.route("/health")
def health():
    return jsonify({"status": "running"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)