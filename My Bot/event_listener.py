# we keep an eye to any changes to the speech stream file
# upon change, we notify related jobs. This is the purpose
# of this module.

import os
import time
from Chatbot import webscrapper
from TTS import TextoSpeech
from playsound import playsound

def webscrapper_onevent(strm):
    webscrapper.send_text_main(strm)

def tts_onevent(strm):
    global TTS_INCREMENT
    TextoSpeech.texttospeech(TTS_INCREMENT)
    playsound(f"TTS/response_{TTS_INCREMENT}.mp3")
    TTS_INCREMENT += 1

STREAMS = [
        ["STT/speech_stream", webscrapper_onevent],
        ["./response_stream", tts_onevent]
        ]

TTS_INCREMENT = 0

if __name__ == "__main__":
    # record inital changetime
    for stream in STREAMS:
        stream_filename = stream[0]
        stream.append(os.path.getmtime(stream_filename))

    while True:
        for stream in STREAMS:
            stream_filename = stream[0]
            callback = stream[1]
            m_time = stream[2]
            if(os.path.getmtime(stream_filename) > m_time):
                f = open(stream_filename, 'r')
                strm = f.read()
                print(strm)
                callback(strm)
                f.close()
                stream[2] = os.path.getmtime(stream_filename)
        time.sleep(0.1)
