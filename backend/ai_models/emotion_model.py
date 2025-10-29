# backend/ai_models/emotion_model.py
# Predicts emotion from given text (temporary logic with confidence scores).

import random

# List of emotions for fallback
EMOTIONS = ["Happy", "Sad", "Angry", "Neutral", "Excited", "Calm"]

def predict_emotion(text: str) -> dict:
    """
    Predicts emotion from text.
    Returns a dictionary with emotion and confidence.
    """
    if not text.strip():
        return {"emotion": "Neutral", "confidence": 0.5}

    keywords = {
        "happy": ("Happy", 0.92),
        "love": ("Excited", 0.90),
        "sad": ("Sad", 0.85),
        "angry": ("Angry", 0.88),
        "calm": ("Calm", 0.83),
        "tired": ("Sad", 0.80)
    }

    # Match keywords
    for word, (emo, conf) in keywords.items():
        if word in text.lower():
            return {"emotion": emo, "confidence": conf}

    # If no keyword found, choose random
    return {
        "emotion": random.choice(EMOTIONS),
        "confidence": round(random.uniform(0.6, 0.85), 2)
    }
