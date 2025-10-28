# backend/ai_models/emotion_model.py

import random

# Temporary list of emotions
EMOTIONS = ["Happy", "Sad", "Angry", "Neutral", "Excited", "Calm"]

def predict_emotion(text: str) -> str:
    """
    Basic dummy emotion predictor.
    Later, this will be replaced by a trained model.
    """
    if not text.strip():
        return "Neutral"

    keywords = {
        "happy": "Happy",
        "sad": "Sad",
        "angry": "Angry",
        "love": "Excited",
        "calm": "Calm"
    }

    for word, emotion in keywords.items():
        if word in text.lower():
            return emotion

    return random.choice(EMOTIONS)
