"""
AUdio to text using google API

pip install SpeechRecognition
sudo apt-get install python-pyaudio python3-pyaudio

pip install PyAudio
sudo apt-get install portaudio19-dev python-all-dev python3-all-dev &&
sudo pip install pyaudio
pip install pyaudio
"""

import speech_recognition as sr

r = sr.Recognizer()
nep_aud = sr.AudioFile('/media/ekbana/ekbana500/randomfiles/nepali Speech/nepali-text-speech/output/combined.wav')
with nep_aud as source:
   audio = r.record(source)
   text = r.recognize_google(audio,language='ne-NP')
   # with open("ff.txt", "w") as f:
   #    f.write(text)
   print(text)

