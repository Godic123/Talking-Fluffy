from itertools import count

#from sqlalchemy import true
from Chatbot import webscrapper
from TTS import TextoSpeech
from STT import transcribe
from playsound import playsound
from Recorder import Recorder

import sys
import os

python_arg = sys.executable

def start():
    recorder = Recorder()
    recorder.listen()
    os.chdir("STT")
    increment = 0
    while True:
        # os = os
        os.system(python_arg + " transcribe.py -t 5")
        webscrapper.getresponse()
        TextoSpeech.texttospeech(increment)
        print(f"file to be played this time: response_{increment}.mp3")
        playsound(f"response_{increment}.mp3")
        increment += 1


start()
