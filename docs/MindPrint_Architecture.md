# MindPrint System Architecture

## Overview
MindPrint is an AI-based emotion tracking system that analyzes voice tone and typing patterns to estimate user mood.

## Core Components
- AI Models: Voice emotion classifier, Typing behavior model  
- Backend: FastAPI API for inference and user data  
- Frontend: React Native app for user interface  
- Database: Stores user emotion history (SQLite or PostgreSQL)
## Data Sources
MindPrint uses emotion datasets from two domains:
- 🎧 **Voice**: RAVDESS, TESS, CREMA-D  
- ⌨️ **Typing**: Keystroke Dynamics, Affect-in-Typing  

Data will be preprocessed to extract emotional features such as:
- Pitch, tone, rhythm (from audio)
- Typing speed, pressure, hesitation patterns (from text)
