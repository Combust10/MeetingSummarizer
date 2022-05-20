import os
from datetime import datetime, date
import transcribe
import subprocess
import time



import pyaudio
import wave
import shutil












CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100
RECORD_SECONDS = 3
WAVE_OUTPUT_FILENAME = "output.wav"

p = pyaudio.PyAudio()

stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                frames_per_buffer=CHUNK)

print("* recording")

frames = []

for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
    data = stream.read(CHUNK)
    frames.append(data)

print("* done recording")

stream.stop_stream()
stream.close()
p.terminate()

wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
wf.setnchannels(CHANNELS)
wf.setsampwidth(p.get_sample_size(FORMAT))
wf.setframerate(RATE)
wf.writeframes(b''.join(frames))
wf.close()

#os.system("python D:\\vsp\pythonProject2\\assemblyai-and-python-in-5-minutes\\transcribe.py D:\\vsp\pythonProject2\\assemblyai-and-python-in-5-minutes\output.wav --local --api_key 964420e2607e4374b3fe3378113b4e5d")
p1=subprocess.Popen(["python","transcribe.py","output.wav","--local","--api_key","964420e2607e4374b3fe3378113b4e5d"]   ,shell=True)
p1.wait()
today = datetime.now()
dateS=str(today.strftime("%c"))
dateS=dateS[4:-5]
dateS=dateS.replace(":","-")
original = r'Transcripts\transcript.txt'
s1=f'Transcripts\\{dateS}.txt'

target = s1
shutil.copyfile(original, target)