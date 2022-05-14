#documentation for python-sounddevice
#https://readthedocs.org/projects/python-sounddevice/downloads/pdf/latest/
#how to install sounddevice
#https://github.com/spatialaudio/python-sounddevice/issues/89

import argparse
import logging
import time
import base64
import json
from time import strftime, gmtime, time_ns
import sys
from kafka import KafkaProducer
from kafka.errors import KafkaError

producer = KafkaProducer(bootstrap_servers='192.168.1.2:9092')#, value_serializer=lambda v: json.dumps(v).encode('utf-8'))
topic = 'mongotest15'

timestamp = time_ns()

#producer1 = KafkaProducer(bootstrap_servers='192.168.1.2:9092', value_serializer=lambda v: json.dumps(v).encode('utf-8'))
#topic1 = 'mongotest16'

def int_or_str(text):
    """Helper function for argument parsing."""
    try:
        return int(text)
    except ValueError:
        return text


parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('-i', '--input-device', type=int_or_str,
                    help='input device ID or substring')
parser.add_argument('-o', '--output-device', type=int_or_str,
                    help='output device ID or substring')
parser.add_argument('-c', '--channels', type=int, default=2,
                    help='number of channels')
parser.add_argument('-t', '--dtype', help='audio data type')
parser.add_argument('-s', '--samplerate', type=float, help='sampling rate')
parser.add_argument('-b', '--blocksize', type=int, help='block size')
parser.add_argument('-l', '--latency', type=float, help='latency in seconds')
args = parser.parse_args()

try:
    import sounddevice as sd

    def callback(indata, frames, time, status):
        if status:
            print(status)

        array: none
        array = indata
        #print(array)

        # Converting the array to bytes.
        byte_encode = array.tobytes()

        print(byte_encode)

        #send to kafka topic
        future = producer.send(topic, value = byte_encode)

        #send to kafka topic info with keyword and timestamp
        #future = producer1.send(topic1, value = {'value': byte_encode.decode('ISO-8859-1'), 'timestamp': timestamp})

    with sd.InputStream(device=(args.input_device),
                   samplerate=args.samplerate, blocksize=args.blocksize,
                   dtype=args.dtype, latency=args.latency,
                   channels=args.channels, callback=callback):
        print('#' * 80)
        print('press Return to quit')
        print('#' * 80)
        input()

except KeyboardInterrupt:
    parser.exit('\nInterrupted by user')
except Exception as e:
    parser.exit(type(e).__name__ + ': ' + str(e))