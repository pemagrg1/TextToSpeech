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
   # text = """दर्शकवृन्द नमस्कार सदाको जस्तै आज पनि yarsagumba अर्को प्रेरणादायी सन्देश लेराएको स्वास्थ्य सन्देशबाट यहाँको जिन्दगीमा सकारात्मक उर्जा थप्न lai 100"""
   # with open("ff.txt", "w") as f:
   #    f.write(text)
   print(text)


# with sr.Microphone() as source:
#     print ("say SOmething")
#     audio = r.listen(source)
#     print ("thanks")
#
# try:
#     print (r.recognize_google(audio,language='hi-IN'))
# except:
#     pass;

"""
#sentiment using textBlob after translating it to english
from textblob import TextBlob
analysis = TextBlob(text)
print(analysis.polarity)
print(analysis.sentiment)
print (analysis.detect_language())
x = analysis.translate(from_lang='ne', to="en")
print (x)
analysis = TextBlob(str(x))
print(analysis.polarity)
print(analysis.sentiment)
print(analysis.detect_language())
"""



