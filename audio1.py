import sounddevice as sd
from scipy.io.wavfile import write
sd.query_devices()
fs=44100
duration=5
print("recording...............")


record_voice=sd.rec(int(duration * fs),samplerate=fs,channels=2)
sd.wait()
write("sound.wav",fs,record_voice)