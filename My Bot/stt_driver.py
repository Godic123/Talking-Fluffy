import os
import sys

if __name__ == "__main__":
    os.chdir("STT")
    os.system(sys.executable + " transcribe.py -t 300")
