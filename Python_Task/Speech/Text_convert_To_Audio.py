from gtts import gTTS
import os

# Text to be converted into speech
text = "Ishu Meri Jan Kya Hal Chal"

# Create a gTTS object
tts = gTTS(text=text, lang='en')

# Save the speech as a file
tts.save("output.mp3")

# Play the speech
os.system("output.mp3")

# First Install gtts : run command inn terminal ==> pip install gtts