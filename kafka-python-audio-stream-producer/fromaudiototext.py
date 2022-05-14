#example of using speech_recognition
#https://realpython.com/python-speech-recognition/

#speech recognise
import speech_recognition as sr

# initialize the recognizer
r = sr.Recognizer()

with sr.Microphone() as source:
    # read the audio data from the default microphone
    audio_data = r.record(source, duration=5)
    print("Recognizing...")
    # convert speech to text
    text = r.recognize_google(audio_data, language = 'ru-RU', show_all = False)
    print(text)
