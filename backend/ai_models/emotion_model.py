# backend/ai_models/emotion_model.py

import random

EMOTIONS = ["Happy", "Sad", "Angry", "Neutral", "Excited", "Calm"]

def predict_emotion(text: str):
    """
    Basic rule-based emotion predictor with confidence score.
    """
    if not text.strip():
        return {"emotion": "Neutral", "confidence": 0.70}

    keywords = {
        "happy": ("Happy", 0.91),
        "sad": ("Sad", 0.85),
        "angry": ("Angry", 0.89),
        "love": ("Excited", 0.92),
        "calm": ("Calm", 0.80),
    }

    for word, (emotion, confidence) in keywords.items():
        if word in text.lower():
            return {"emotion": emotion, "confidence": confidence}

    # If no keyword matches, pick random neutral emotion
    emotion = random.choice(EMOTIONS)
    return {"emotion": emotion, "confidence": 0.70}
