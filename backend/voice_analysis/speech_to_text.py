# backend/voice_analysis/speech_to_text.py
# Converts a speech (audio) file to text using Google Speech Recognition API.

import speech_recognition as sr

def speech_to_text(audio_file_path: str) -> str:
    """
    Converts the given audio file into text.
    Supported formats: WAV, FLAC, AIFF
    Returns the recognized text as a string.
    """
    recognizer = sr.Recognizer()
    try:
        with sr.AudioFile(audio_file_path) as source:
            audio_data = recognizer.record(source)
            text = recognizer.recognize_google(audio_data)
            return text
    except sr.UnknownValueError:
        return "Could not understand audio"
    except sr.RequestError:
        return "Speech recognition service unavailable"
    except Exception as e:
        return f"Error: {str(e)}"
