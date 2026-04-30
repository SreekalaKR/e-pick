import pyttsx3
import speech_recognition as sr
import threading

engine = pyttsx3.init()
engine.setProperty('rate', 175)
engine.setProperty('volume', 1.0)


# 🔊 GUARANTEED VOICE OUTPUT (NON-BLOCKING)
def speak(text):
    def run():
        try:
            print("EPick:", text)
            engine.say(text)
            engine.runAndWait()
        except Exception as e:
            print("Speech error:", e)

    threading.Thread(target=run, daemon=True).start()


def take_command():
    r = sr.Recognizer()

    r.energy_threshold = 400
    r.dynamic_energy_threshold = True
    r.pause_threshold = 1.5

    with sr.Microphone() as source:
        print("Listening...")
        r.adjust_for_ambient_noise(source, duration=1)

        try:
            audio = r.listen(source, timeout=None, phrase_time_limit=10)
        except:
            return "none"

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="en-in")
        print("You said:", query)
        return query.lower().strip()

    except:
        return "none"