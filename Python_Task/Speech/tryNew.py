import speech_recognition as sr
from gtts import gTTS
import os

# Initialize the recognizer
recognizer = sr.Recognizer()

# Use the default microphone as the audio source
with sr.Microphone() as source:
    print("Listening...")

    # Adjust ambient noise levels for better recognition
    recognizer.adjust_for_ambient_noise(source)

    # Listen for speech
    audio = recognizer.listen(source)

    print("Recognizing...")

    try:
        # Use Google Speech Recognition to convert speech to text
        text = recognizer.recognize_google(audio)
        if text == "Elvis bhai" :
            text="Elvis bhai Ke aage koi Bol Sakta Hai Kya"
            tts = gTTS(text=text, lang='en')
            tts.save("output.mp3")
            os.system("output.mp3")
        else : 
            print("You said:", text)
    except sr.UnknownValueError:
        print("Sorry, could not understand audio.")
    except sr.RequestError as e:
        print("Error occurred; {0}".format(e))