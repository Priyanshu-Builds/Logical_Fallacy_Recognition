import speech_recognition as sr
from prompt import execute_prompt  # Ensure this is pointing to the correct file

r = sr.Recognizer()

def record_audio():
    with sr.Microphone() as source2:
        print("Listening...")
        audio2 = r.listen(source2)
        print("Finished listening.")
    return audio2

def output_text(text):
    with open("output.txt", "a") as f:
        f.write(text + "\n")

def real_time_with_microphone():
    # Clear the output file at the beginning
    with open("output.txt", "w") as f:
        f.truncate(0)

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

    # Call the main() function from the prompt module after recording finishes
    execute_prompt()

# Start the real-time recording process
#real_time_with_microphone()
