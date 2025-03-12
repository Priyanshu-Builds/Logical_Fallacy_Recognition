import pyaudio
import wave
import realtime_speech as sr

# Audio recording settings
CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100
RECORD_SECONDS = 10  # Adjust duration as needed
WAVE_OUTPUT_FILENAME = "output.wav"

# Record system audio
p = pyaudio.PyAudio()
stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                input_device_index=None,  # Use default input device (VB-Audio Virtual Cable)
                frames_per_buffer=CHUNK)

print("* recording")
frames = []
for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
    data = stream.read(CHUNK)
    frames.append(data)

print("* done recording")

stream.stop_stream()
stream.close()
p.terminate()

# Save the recorded audio to a file
wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
wf.setnchannels(CHANNELS)
wf.setsampwidth(p.get_sample_size(FORMAT))
wf.setframerate(RATE)
wf.writeframes(b''.join(frames))
wf.close()

# Transcribe the audio using Google Speech-to-Text
r = sr.Recognizer()
with sr.AudioFile(WAVE_OUTPUT_FILENAME) as source:
    audio = r.record(source)

try:
    text = r.recognize_google(audio)
    print("Transcription:", text)
    with open("output.txt", "a") as f:
        f.write(text + "\n")
except sr.UnknownValueError:
    print("Google Speech Recognition could not understand the audio")
except sr.RequestError as e:
    print(f"Could not request results from Google Speech Recognition service; {e}")