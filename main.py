#!/usr/bin/python
# vim encoding: utf-8
import os
from dotenv import load_dotenv,find_dotenv
load_dotenv(find_dotenv(), override=True)
PROJECT_PATH = os.environ.get("PROJECTPATH")

import _thread as thread
import time
import wave
import pyaudio
from pydub import AudioSegment

class Speak:
    def __init__(self,string):
        self.database = self.listfiles(PROJECT_PATH+"data/nepali_sounds/")
        self.play(string)

    def listfiles(self,dirs):
        for root, dirs, files in os.walk(dirs):
            pass
        return files

    def part(self,string):
        """
        breaks nepali string into  characters and returns the list of characters
        note:one nepali character is  made of three ascii characters
        """
        characters = []
        count = 0
        st = ""
        for char in string:
            if char == " ":
                characters.append("space")
            elif char == "?" or char == "," or char == ";" or char == ":":
                characters.append(char)
                count = 0
            else:
                # st += char
                # count += 1
                characters.append(char)

            if count == 3:
                characters.append(st)
                st = ""
                count = 0
        return characters

    def letters(self,characters):
        """
        returns list of letters formed by  characters
        """
        letters = ["क", "ख", "ग", "घ", "ड॒", "च", "छ", "ज", "झ", "ञ", "ट", "ठ",
                   "ड", "ढ", "ण", "त", "थ", "द", "ध", "न", "प", "फ", "ब", "भ",
                   "म", "य", "र", "ल", "व", "श", "ष", "स", "ह", "अ", "आ", "इ",
                   "ई", "उ", "ऊ", "ए", "ऐ", "ओ"]
        shabda = []
        st = ""
        for ch in characters:
            if ch == "space":
                shabda.append(st)
                st = ""
                shabda.append(ch)
            else:
                if ch in letters:
                    if st != "":
                        shabda.append(st)
                    st = ch
                else:
                    st += ch

        shabda.append(st)
        for i, ch in enumerate(shabda):
            # if i == len(shabda)-1:
            #     shabda[i] = ch+"।"
            if ch == "":
                shabda.remove(ch)
        print(shabda)
        return shabda


    def play(self,string):
        """
        starts thread to play the sound
        """
        letters = self.letters(self.part(string))
        delay = 0.17
        combined = AudioSegment.empty()
        for l in letters:
            sound = l+".wav"
            if sound in self.database:
                # print(sound)
                # self.playsound(sound,delay)
                thread.start_new_thread(self.playsound,(sound,delay))
                time.sleep(delay)
                #delay = 0.6
                order = AudioSegment.from_file(PROJECT_PATH+"data/nepali_sounds/"+sound)
                # extract = order[0:5000]
                combined += order


        combined.export(PROJECT_PATH+"output/"+string+".wav", format='wav')

    def playsound(self,sound,delay):
        """
        plays the sound
            this code is from docs of pyaudio
            https://people.csail.mit.edu/hubert/pyaudio/docs/
        """
        try:
            CHUNK = 1024
            #time.sleep(delay)
            wf = wave.open(PROJECT_PATH+"data/nepali_sounds/"+sound, 'rb')
            print ()
            #instantiate pyaudio
            p = pyaudio.PyAudio()

            #open stream
            stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                            channels=wf.getnchannels(),
                            rate=wf.getframerate(),
                            output=True)
            #read data
            data = wf.readframes(CHUNK)

            #play stream
            while data:
                stream.write(data)
                data = wf.readframes(CHUNK)

            #stop stream
            stream.stop_stream()
            stream.close()

            #close pyaudio
            p.terminate()
            return
        except Exception as e:
            #    pass
            print (e)


if __name__ == "__main__":
    try:
        # a = Speak(sys.argv[1])
        a = Speak("समाचार के छ")
        # a.play()

    except Exception as e:
        print (e)