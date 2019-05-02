#!/usr/bin/python
# vim encoding: utf-8
import sys
import _thread as thread


import time
import wave
import pyaudio
import modules.parts as parts
import modules.loadsound as loadsound
from pydub import AudioSegment
import librosa


class Speak:
    def __init__(self,string):
        self.database = loadsound.listfiles("sounds/");
        self.letters = parts.letters(parts.part(string))
        self.play()
    def play(self):
        """
        starts thread to play the sound
        """
        delay = 0.17
        combined = AudioSegment.empty()
        for l in self.letters:
            sound = l+".wav"
            if sound in self.database:
                # print(sound)
                # self.playsound(sound,delay)
                thread.start_new_thread(self.playsound,(sound,delay))
                time.sleep(delay)
                #delay = 0.6
                order = AudioSegment.from_file("./sounds/"+sound)
                combined += order


        combined.export("/media/ekbana/ekbana500/randomfiles/nepali Speech/nepali-text-speech/output/combined1.wav", format='wav')

    def playsound(self,sound,delay):
        """
        plays the sound
            this code is from docs of pyaudio 
            https://people.csail.mit.edu/hubert/pyaudio/docs/
        """
        try:
            CHUNK = 1024
            #time.sleep(delay)
            wf = wave.open("sounds/"+sound, 'rb')
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