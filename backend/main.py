# MindPrint Backend - Day 3 Update
# Author: Muzammil Rehman
# Description: Basic API setup for text emotion analysis.

from flask import Flask, jsonify, request
from utils.text_preprocessor import clean_text

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({"message": "Welcome to MindPrint API v1.1"}), 200


@app.route('/analyze_text', methods=['POST'])
def analyze_text():
    try:
        data = request.get_json()
        text = data.get('text', '')

        if not text:
            return jsonify({"error": "No text provided"}), 400

        # Step 1: Clean the text
        cleaned = clean_text(text)

        # Step 2: Mock emotion logic (temporary)
        if "happy" in cleaned or "love" in cleaned:
            mood = "happy"
            confidence = 0.92
        elif "sad" in cleaned or "tired" in cleaned:
            mood = "sad"
            confidence = 0.81
        else:
            mood = "neutral"
            confidence = 0.70

        # Step 3: Return mock response
        return jsonify({
            "original_text": text,
            "cleaned_text": cleaned,
            "mood": mood,
            "confidence": confidence
        }), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True)
