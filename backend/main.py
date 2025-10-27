# MindPrint Backend - Starter Template
# Author: Muzammil Rehman
# Description: Backend entry point for MindPrint AI project.

from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({"message": "Welcome to MindPrint API v1.0"}), 200

if __name__ == '__main__':
    app.run(debug=True)
