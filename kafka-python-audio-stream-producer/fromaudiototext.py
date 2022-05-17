#example of using speech_recognition
#https://realpython.com/python-speech-recognition/

#speech recognise
import speech_recognition
import pyttsx3

# initialize the recognizer
r = speech_recognition.Recognizer()

while True:

    try:

        with speech_recognition.Microphone(13) as source:

            r.adjust_for_ambient_noise(source, duration=0.2)
            audio = r.listen(source)

            text = r.recognize_google(audio)
            text = text.lower()

            print(f"Recognized {text}")

            if 'what is your name' in text:
                print('My name is PatientCare')

    except speech_recognition.UnknownValueError:

        r = speech_recognition.Recognizer()
        continue

