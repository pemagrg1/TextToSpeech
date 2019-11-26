#!/usr/bin/python
# vim encoding: utf-8
import os
from dotenv import load_dotenv,find_dotenv
load_dotenv(find_dotenv(), override=True)
PROJECT_PATH = os.environ.get("PROJECTPATH")

import re
import wave
import pyaudio
import _thread
import time
from pydub import AudioSegment


class TextToSpeech:
    
    CHUNK = 1024

    def __init__(self, words_pron_dict:str = 'cmudict-0.7b.txt'):
        self._l = {}
        self._load_words(words_pron_dict)

    def _load_words(self, words_pron_dict:str):
        with open(words_pron_dict, 'r') as file:
            for line in file:
                if not line.startswith(';;;'):
                    key, val = line.split('  ',2)
                    self._l[key] = re.findall(r"[A-Z]+",val)

    def get_pronunciation(self, str_input):
        list_pron = []
        for word in re.findall(r"[\w']+",str_input.upper()):
            if word in self._l:
                list_pron += self._l[word]
        print(list_pron)
        delay=0
        combined = AudioSegment.empty()
        for pron in list_pron:
            sound = pron.lower() + ".wav"
            _thread.start_new_thread(self.play_audio, (sound,delay))
            delay += 0.145
            order = AudioSegment.from_file(PROJECT_PATH + "EnglishTextToSpeech/sounds/" + sound)
            # extract = order[0:5000]
            combined += order

        # combined.export(PROJECT_PATH + "EnglishTextToSpeech/output/combined1.wav",
        #                 format='wav')

    def play_audio(self,sound, delay):
        try:
            print ("----")
            time.sleep(delay)
            wf = wave.open(PROJECT_PATH+"EnglishTextToSpeech/sounds/"+sound, 'rb')
            p = pyaudio.PyAudio()
            stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                            channels=wf.getnchannels(),
                            rate=wf.getframerate(),
                            output=True)
            
            data = wf.readframes(TextToSpeech.CHUNK)
            print("==",data)
            while data:
                stream.write(data)
                data = wf.readframes(TextToSpeech.CHUNK)
                print(type(data))
        
            stream.stop_stream()
            stream.close()

            p.terminate()
            return
        except:
            pass
    
 
 

if __name__ == '__main__':
    tts = TextToSpeech()
    tts.get_pronunciation("ga")
