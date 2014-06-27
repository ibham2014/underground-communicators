#import datetime
import re
#from app_utils import getTimezone
#from semantic.dates import DateService
import os
import json
from wave import open as open_audio
import audioop
import pyaudio
import alteration

WORDS = ["RECORD"]


def handle(text, mic, profile):
    """
        Reports the current time based on the user's timezone.

        Arguments:
        text -- user-input, typically transcribed speech
        mic -- used to interact with the user (for both input and output)
        profile -- contains information related to the user (e.g., phone number)
    """

    #tz = getTimezone(profile)
    #now = datetime.datetime.now(tz=tz)
    #service = DateService()
    #response = service.convertTime(now)
    mic.say("I AM RECORDING.")
    os.system("arecord -d 3 -f cd /home/pi/jasper/client/modules/recordings/test1.wav")
    os.system("aplay /home/pi/jasper/client/modules/recordings/test1.wav")

def isValid(text):
    """
        Returns True if input is related to the time.

        Arguments:
        text -- user-input, typically transcribed speech
    """
    return bool(re.search(r'\brecord\b', text, re.IGNORECASE))








