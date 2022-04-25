from STT import transcribe

import sys
import os
import subprocess

if __name__ == "__main__":
    subprocess.Popen([sys.executable, "stt_driver.py"])
    # note: stt_event_listener will decide when to run webscrapper, tts, playsound
    subprocess.Popen([sys.executable, "event_listener.py"])


