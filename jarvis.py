import pyttsx3
import speech_recognition as sr
import datetime
import webbrowser
import wikipedia

engine = pyttsx3.init()

def speak(text):
    print("Jarvis:", text)
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
        command = r.recognize_google(audio, language="en-IN")
        print("You:", command)
        return command.lower()

    except:
        return ""

def wish():
    hour = datetime.datetime.now().hour

    if hour < 12:
        speak("Good Morning")
    elif hour < 18:
        speak("Good Afternoon")
    else:
        speak("Good Evening")

    speak("I am Jarvis. How can I help you?")

wish()

while True:
    query = take_command()

    if "youtube" in query:
        webbrowser.open("https://youtube.com")
        speak("Opening YouTube")

    elif "google" in query:
        webbrowser.open("https://google.com")
        speak("Opening Google")

    elif "time" in query:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"The time is {current_time}")

    elif "wikipedia" in query:
        speak("Searching Wikipedia")
        topic = query.replace("wikipedia", "")
        result = wikipedia.summary(topic, sentences=2)
        speak(result)

    elif "stop" in query or "exit" in query:
        speak("Goodbye")
        break