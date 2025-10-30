# MindPrint Backend - Full Integration
# Author: Muzammil Rehman
# Description: Flask API + Frontend Integration for Emotion Analysis

from flask import Flask, request, jsonify, render_template
from ai_models.emotion_model import predict_emotion
from flask_cors import CORS

# ---------------------- APP SETUP ----------------------
app = Flask(
    __name__,
    static_folder="static",       # for CSS, JS, images
    template_folder="templates"   # for HTML files
)
CORS(app)

# ---------------------- FRONTEND ROUTE ----------------------
@app.route("/")
def home():
    """
    Serves the main frontend page (index.html)
    """
    return render_template("index.html")

# ---------------------- API ROUTE ----------------------
@app.route("/analyze_text", methods=["POST"])
def analyze_text():
    """
    Receives user text, predicts emotion, and returns result as JSON
    """
    try:
        data = request.get_json()
        text = data.get("text", "").strip()

        if not text:
            return jsonify({"error": "No text provided"}), 400

        emotion = predict_emotion(text)

        return jsonify({"emotion": emotion}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500


# ---------------------- MAIN ENTRY POINT ----------------------
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
