from itertools import count
from Chatbot import webscrapper
from TTS import TextoSpeech
from STT import transcribe
from playsound import playsound
import os

def start():
    systemCall = os
    systemCall.chdir("C:\\Users\\StevenLi\\Desktop\\My Bot\\STT")
    systemCall.system("py transcribe.py -t 5")
    webscrapper.getresponse()
    TextoSpeech.texttospeech()
    playsound("C:\\Users\\StevenLi\\Desktop\\My Bot\\STT\\response.mp3")


start()
