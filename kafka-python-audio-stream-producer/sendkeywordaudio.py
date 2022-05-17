#example of using speech_recognition
#https://realpython.com/python-speech-recognition/

#speech recognise
import speech_recognition
import pyttsx3

import json
import time
from time import time_ns

import argparse

from kafka import KafkaProducer
from kafka.errors import KafkaError

producer = KafkaProducer(bootstrap_servers='192.168.1.12:9092', value_serializer=lambda v: json.dumps(v).encode('utf-8'))
topic = 'mongotest16'

timestamp = time_ns()

parser = argparse.ArgumentParser()
parser.add_argument('-i', type=int, help='input device ID or substring')
args = parser.parse_args()

def fnc1():
    r = speech_recognition.Recognizer()

    with speech_recognition.Microphone(args.i) as source:

        a = ''
        r.adjust_for_ambient_noise(source, duration=0.2)
        audio = r.listen(source)

        try:

            a = r.recognize_google(audio)
            a = a.lower()

            print(f"Recognized {a}")

        except:
            if speech_recognition.UnknownValueError:
                print('Unable to recognize speech')
                r = speech_recognition.Recognizer()

        return a

def respond(voice_data_a):
    if "what's your name" in voice_data_a:
        print('My name is PatientCare')
    elif "what is your name" in voice_data_a:
        print('My name is PatientCare')

def keyword_to_kafka(keyword):
    if 'open' in keyword:
        print (f"Sent keyword {keyword} on kafka topic")
        #send to kafka topic info with keyword and timestamp
        future = producer.send(topic, value = {'keyword': keyword, 'timestamp': timestamp})

while True:
    voice_data_a = fnc1()
    respond(voice_data_a)
    keyword_to_kafka(voice_data_a)