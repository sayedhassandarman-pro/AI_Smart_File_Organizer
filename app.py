from flask import Flask, request, jsonify, render_template
import sqlite3
from ai_model import AIModel
from db import init_db

app = Flask(__name__)
model = AIModel()

init_db()

def db():
    return sqlite3.connect("users.db")

# ---------------- HOME ---------------- #
@app.route("/")
def home():
    return render_template("index.html")

# ---------------- REGISTER ---------------- #
@app.route("/register", methods=["POST"])
def register():
    data = request.json

    conn = db()
    c = conn.cursor()

    c.execute("INSERT INTO users (username, password) VALUES (?, ?)",
              (data["username"], data["password"]))

    conn.commit()
    conn.close()

    return jsonify({"message": "User ثبت شو"})

# ---------------- LOGIN ---------------- #
@app.route("/login", methods=["POST"])
def login():
    data = request.json

    conn = db()
    c = conn.cursor()

    c.execute("SELECT * FROM users WHERE username=? AND password=?",
              (data["username"], data["password"]))

    user = c.fetchone()
    conn.close()

    if user:
        return jsonify({"message": "Login کامیاب شو"})
    else:
        return jsonify({"message": "Login غلط دی"})

# ---------------- AI PREDICT ---------------- #
@app.route("/predict", methods=["POST"])
def predict():
    data = request.json
    file_name = data["file_name"]

    category = model.predict(file_name)

    return jsonify({
        "file": file_name,
        "category": category
    })

if __name__ == "__main__":
    app.run(debug=True)