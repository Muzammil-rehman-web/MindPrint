# MindPrint Backend - Day 4 Update
# Author: Muzammil Rehman
# Description: Flask API integrated with AI Emotion Model.

from flask import Flask, jsonify, request
import base64
import os
import uuid

# Local module imports
from utils.text_preprocessor import clean_text
from ai_models.emotion_model import predict_emotion
from voice_analysis.speech_to_text import speech_to_text

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({"message": "Welcome to MindPrint API v1.2 (AI Integrated)"}), 200


@app.route('/analyze_text', methods=['POST'])
def analyze_text():
    try:
        data = request.get_json()
        text = data.get('text', '')

        if not text:
            return jsonify({"error": "No text provided"}), 400

        # Step 1: Clean text
        cleaned = clean_text(text)

        # Step 2: Predict emotion using our new AI model ✅
        emotion = predict_emotion(cleaned)

        # Step 3: Temporary confidence score
        confidence = 0.80

        # Step 4: Return structured response
        return jsonify({
            "original_text": text,
            "cleaned_text": cleaned,
            "predicted_emotion": emotion,
            "confidence": confidence
        }), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True)
