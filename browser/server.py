from flask import Flask, send_file
from flask_cors import CORS
import os
import random

app = Flask(__name__)
CORS(app) 
audio_folder = "/home/muzz11/Desktop/assign1/browser/audio"

@app.route('/play')
def play_random_audio():
    audio_files = [f for f in os.listdir(audio_folder) if f.endswith(".mp3")]
    if not audio_files:
        return "No audio files found."

    random_audio = random.choice(audio_files)
    return send_file(os.path.join(audio_folder, random_audio))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

