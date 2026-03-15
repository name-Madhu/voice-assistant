import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import wikipedia

engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print("You said:", query)
    except:
        print("Could not understand")
        return ""

    return query.lower()

def run_assistant():

    speak("Hello, I am your voice assistant")

    while True:
        query = take_command()

        if "time" in query:
            time = datetime.datetime.now().strftime("%H:%M")
            speak("The time is " + time)

        elif "open google" in query:
            webbrowser.open("https://www.google.com")
            speak("Opening Google")

        elif "open youtube" in query:
            webbrowser.open("https://www.youtube.com")
            speak("Opening YouTube")

        elif "wikipedia" in query:
            speak("Searching Wikipedia")
            query = query.replace("wikipedia", "")
            result = wikipedia.summary(query, sentences=2)
            speak(result)
            print(result)

        elif "stop" in query or "exit" in query:
            speak("Goodbye")
            break

run_assistant()
