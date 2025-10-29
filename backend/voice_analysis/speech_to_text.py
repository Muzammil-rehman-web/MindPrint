# backend/voice_analysis/speech_to_text.py
# Author: Muzammil Rehman
# Description: Converts voice input (audio) to text using speech recognition.

import speech_recognition as sr

def convert_speech_to_text(audio_path: str):
    """
    Converts an audio file to text using SpeechRecognition.
    """
    recognizer = sr.Recognizer()
    try:
        with sr.AudioFile(audio_path) as source:
            audio = recognizer.record(source)
            text = recognizer.recognize_google(audio)
            return {"text": text, "status": "success"}
    except Exception as e:
        return {"error": str(e), "status": "failed"}

