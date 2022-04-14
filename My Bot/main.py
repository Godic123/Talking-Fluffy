from itertools import count

from sqlalchemy import true
from Chatbot import webscrapper
from TTS import TextoSpeech
from STT import transcribe
from playsound import playsound
from Recorder import Recorder
import os

def start():
    recorder = Recorder.Recorder()
    istrue = recorder.listen()
    if(istrue):
        while true:
            systemCall = os
            systemCall.chdir("C:\\Users\\StevenLi\\Desktop\\My Bot\\STT")
            systemCall.system("py transcribe.py -t 5")
            webscrapper.getresponse()
            TextoSpeech.texttospeech()
            playsound("C:\\Users\\StevenLi\\Desktop\\My Bot\\STT\\response.mp3")


start()
