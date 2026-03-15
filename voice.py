from gtts import gTTS
import datetime
import webbrowser
import os

def speak(text):
    print("Assistant:", text)

    tts = gTTS(text=text, lang="en")
    tts.save("voice.mp3")

    os.startfile("voice.mp3")   # plays the audio on Windows

def assistant():
    while True:
        command = input("Enter your command: ").lower()

        if "hello" in command:
            speak("Hello , how can I help you today")

        elif "time" in command:
            time = datetime.datetime.now().strftime("%H:%M")
            speak(f"The current time is {time}")

        elif "date" in command:
            date = datetime.datetime.now().strftime("%d %B %Y")
            speak(f"Today's date is {date}")

        elif "open google" in command:
            speak("Opening Google")
            webbrowser.open("https://www.google.com")

        elif "open youtube" in command:
            speak("Opening YouTube")
            webbrowser.open("https://www.youtube.com")

        elif "exit" in command:
            speak("Goodbye ")
            break

        else:
            speak("Sorry, I did not understand the command")

assistant()
