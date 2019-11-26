"""
sudo apt-get install python3 python3-all-dev python3-pip build-essential swig git libpulse-dev
pip install pocketsphinx
pip install SpeechRecognition
sudo apt-get install libasound-dev portaudio19-dev libportaudio2 libportaudiocpp0

sudo apt-get install ffmpeg libav-tools

sudo apt-get install python-pyaudio

pip install pyaudio
python -m speech_recognition

downlaod models from: https://sourceforge.net/projects/cmusphinx/files/Acoustic%20and%20Language%20Models/
move the folder to pocket phoenix
"""
#
# import speech_recognition as sr
#
# r = sr.Recognizer()
# nep_aud = sr.AudioFile('/media/ekbana/ekbana500/DOWNLOAD/short hindi speech.wav')
#
# # #using google
# # # with nep_aud as source:
# # #    audio = r.record(source)
# # #    text = r.recognize_google(audio,language='hi-IN')
# # #    print(text)
#
# #using Sphinx
# with nep_aud as source:
#    audio = r.record(source)
#    text = r.recognize_sphinx(audio,language='hi-IN')
#    print(text)
#

# !/usr/bin/env python3

import speech_recognition as sr

# obtain path to "english.wav" in the same folder as this script
from os import path

AUDIO_FILE = '/media/ekbana/ekbana500/DOWNLOAD/short hindi speech.wav'
# AUDIO_FILE = path.join(path.dirname(path.realpath(__file__)), "french.aiff")
# AUDIO_FILE = path.join(path.dirname(path.realpath(__file__)), "chinese.flac")

# use the audio file as the audio source
r = sr.Recognizer()
with sr.AudioFile(AUDIO_FILE) as source:
   audio = r.record(source)  # read the entire audio file

# recognize speech using Sphinx
print ("===recognizing===")
try:
   print("Sphinx thinks you said ::: " + r.recognize_sphinx(audio,"hi-IN"))
except sr.UnknownValueError:
   print("Sphinx could not understand audio")
except sr.RequestError as e:
   print("Sphinx error; {0}".format(e))