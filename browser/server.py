from flask import Flask, send_file, request
from flask_cors import CORS
import os
import random

app = Flask(__name__)
CORS(app) 
audio_folder = "audio"

@app.route('/play')
def play_random_audio():
    audio_files = [f for f in os.listdir(audio_folder) if f.endswith(".mp3")]
    if not audio_files:
        return "No audio files found."

    random_audio = random.choice(audio_files)
    audio = request.args.get('songname')
    print("Audio name", audio)
    if(audio):
        return send_file(os.path.join(audio_folder, audio))
    else:
        return send_file(os.path.join(audio_folder, random_audio))


@app.route('/app')
def static_file():
    return send_file("index2.html")

@app.route('/songs')
def get_songs():
    audio_files = [f for f in os.listdir(audio_folder) if f.endswith(".mp3")]
    random.shuffle(audio_files)
    return audio_files

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

