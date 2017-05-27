import speech_recognition as speech
from os import path
import webbrowser
AUDIO_FILE = path.join(path.dirname(path.realpath(__file__)), "google.wav")

object_speech = speech.Recognizer()
with speech.AudioFile(AUDIO_FILE) as source:
    audio = object_speech.record(source)  # read the entire audio file

try:
    
    print("Google Speech Recognition thinks you said " + object_speech.recognize_google(audio))
    #url_to_open = "https://www.google.com"
    availed_text = object_speech.recognize_google(audio)
    data = availed_text.split(" ")
    website_name = data[1]
    url_to_open = "https://www." + website_name
    webbrowser.open(url_to_open)
    print " Attack successful"

except speech.UnknownValueError:
    print("Google Speech Recognition could not understand audio")
except speech.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))

