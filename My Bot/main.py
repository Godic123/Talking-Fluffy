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
    while True:
        # os = os
        os.chdir("STT")
        os.system(python_arg + " transcribe.py -t 5")
        webscrapper.getresponse()
        TextoSpeech.texttospeech()
        playsound("response.mp3")


start()
