from flask import Flask, request, jsonify

app = Flask(__name__)

# Temporary in-memory data
users = [
    {"id": 1, "name": "Alice"},
    {"id": 2, "name": "Bob"}
]

# GET: Retrieve all users
@app.route("/users", methods=["GET"])
def get_users():
    return jsonify(users), 200


# POST: Add a new user
@app.route("/users", methods=["POST"])
def create_user():
    data = request.get_json(silent=True)

    if not data or not data.get("name"):
        return jsonify({"error": "Name is required"}), 400

    new_user = {
        "id": max((user["id"] for user in users), default=0) + 1,
        "name": data["name"]
    }

    users.append(new_user)

    return jsonify(new_user), 201


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)