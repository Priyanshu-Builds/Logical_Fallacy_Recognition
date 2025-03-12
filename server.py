from flask import Flask, render_template, request, redirect, url_for
import realtime_speech as speech_main
from youtube_video import process_youtube_link

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if 'record_audio' in request.form:
            # Handle recording audio
            result = speech_main.record_audio()  # Call your function from main.py
            return render_template('result.html', result=result)
        elif 'youtube_link' in request.form:
            # Handle processing YouTube link
            youtube_url = request.form['youtube_url']
            result = process_youtube_link(youtube_url)  # Call your function from youtube_video.py

            # Pass variables with correct dictionary keys
            return render_template('result.html', youtube_url=result['youtube_url'], fallacy=result['fallacy'])
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
