import webbrowser
import datetime
from engine import speak
from ai_brain import get_ai_response


def handle_command(query):
    query = query.lower()

    if "youtube" in query:
        response = "Opening YouTube"
        speak(response)
        webbrowser.open("https://youtube.com")
        return response

    if "google" in query:
        response = "Opening Google"
        speak(response)
        webbrowser.open("https://google.com")
        return response

    if "time" in query:
        t = datetime.datetime.now().strftime("%H:%M:%S")
        response = f"The time is {t}"
        speak(response)
        return response

    if "exit" in query:
        speak("Goodbye")
        exit()

    # 🤖 AI RESPONSE
    response = get_ai_response(query)

    if not response:
        response = "Sorry, I didn't understand that."

    print("AI:", response)
    speak(response)

    return response