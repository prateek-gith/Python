import speech_recognition as sr

# Create a Recognizer instance
recognizer = sr.Recognizer()

# Use the default microphone as the audio source
with sr.Microphone() as source:
    print("Say something:")
    recognizer.adjust_for_ambient_noise(source)
    
    try:
        # Listen with a timeout of 5 seconds
        audio_data = recognizer.listen(source, timeout=5, phrase_time_limit=10)
        # recognizer.pause_threshold=0.5
        
        # Recognize speech using Google Web Speech API
        text = recognizer.recognize_google(audio_data)
        # query = recognizer.recognize_sphinx(audio_data)
        print("Google Speech Recognition thinks you said: " + text)
        
    except sr.WaitTimeoutError:
        print("Listening timed out")
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand the audio")
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")
