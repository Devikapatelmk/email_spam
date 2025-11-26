from flask import Flask, request, jsonify, send_from_directory
import joblib
import os

app = Flask(__name__, static_folder="static")

model = joblib.load("models/spam_model.pkl")
vectorizer = joblib.load("models/vectorizer.pkl")

@app.route("/")
def home():
    return send_from_directory(app.static_folder, "index.html")

@app.route("/predict", methods=["POST"])
def predict():
    text = request.form.get("text")
    if not text:
        return jsonify({"error": "No text provided"}), 400

    vector = vectorizer.transform([text])
    result = model.predict(vector)[0]

    return jsonify({"result": "Spam" if result == 1 else "Not Spam"})

if __name__ == "__main__":
    app.run(debug=True)
