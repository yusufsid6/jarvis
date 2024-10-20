import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak("Good Morning!")

    elif 12 <= hour < 18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("Hello sir, I am Jarvis. Please tell me how may I help you")


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print("Say that again please...")
        return "None"
    return query


def sendEmail(to, content):
    # Your email sending code goes here (same as your existing code)
    pass


if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()

        if 'wikipedia' in query:
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("https://www.youtube.com")

        elif 'open google' in query:
            webbrowser.open("https://www.google.com")
            speak("What should I search on Google?")
            content = takeCommand()

            if content:
                webbrowser.open(f"https://www.google.com/search?q={content}")
                speak(f"Here are the search results for {content}.")

        elif 'open project file' in query:
            project_file_path = '"D:\YUSUF SID.pdf"'
            os.startfile(project_file_path)
            speak("Opening the project file.")

        elif 'play music' in query:
            music_dir = 'C:\\Users\\Lenovo\\Music\\favourite'
            songs = os.listdir(music_dir)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif 'open code' in query:
            codePath = '"C:\\Users\\Lenovo\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"'
            os.startfile(codePath)

        elif 'email to yusuf' in query:
            speak("What should I say?")
            content = takeCommand()
            to = "yusufsid87842@gmail.com"
            sendEmail(to, content)
            speak("Email has been sent!")

        elif 'thank you' in query:
            speak("you are welcome sir")

        elif 'exit' in query:
            speak("Goodbye sir")
            break
    

  
