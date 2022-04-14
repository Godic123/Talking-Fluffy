from itertools import count
from Chatbot import webscrapper
from TTS import TextoSpeech
from STT import transcribe
from playsound import playsound
import pyaudio
import math
import struct

Threshold = 10

SHORT_NORMALIZE = (1.0/32768.0)
chunk = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 16000
swidth = 2

TIMEOUT_LENGTH = 5

def start():

    webscrapper.getresponse()
    TextoSpeech.texttospeech()
    playsound("C:\\Users\\StevenLi\\Desktop\\My Bot\\response.mp3")


start()
