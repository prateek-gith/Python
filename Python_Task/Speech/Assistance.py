import speech_recognition as sr
import pyttsx3
import datetime
# import wikipedia
import webbrowser
import os

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  # You can change the voice index based on your preference

def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    try:
        with sr.Microphone() as source:
            print("Listening...")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'assistant' in command:
                command = command.replace('assistant', '')
                print("User:", command)
    except:
        pass
    return command

def run_assistant():
    command = take_command()
    if 'time' in command:
        time = datetime.datetime.now().strftime("%H:%M")
        talk(f"The current time is {time}")
    elif 'search' in command:
        search_term = command.replace('search', '')
        webbrowser.open_new_tab(f"https://www.google.com/search?q={search_term}")
    elif 'open' in command:
        app = command.replace('open', '')
        os.system(f"start {app}")
    elif 'quit' in command:
        talk("Goodbye!")
        exit()
    else:
        talk("I'm sorry, I didn't understand that command.")

run_assistant()
