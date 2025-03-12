import sounddevice as sd
import speech_recognition as sr

r = sr.Recognizer()

def record_audio():
    print("Listening...")
    audio = sd.rec(int(10 * 44100), samplerate=44100, channels=2)
    sd.wait()
    print("Finished listening.")
    return audio[:, 0]  # Use only the first channel for mono audio

def output_text(text):
    with open("output.txt", "a") as f:
        f.write(text + "\n")

try:
    while True:
        audio = record_audio()
        try:
            text = r.recognize_google(audio)
            output_text(text)
            print("Wrote text:", text)
            if text.lower() == "exit":
                break
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand the audio")
except KeyboardInterrupt:
    print("\nProgram interrupted by user. Exiting gracefully.")
