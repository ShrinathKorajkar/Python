#! python3
# countdown.py - A simple countdown script.

import time, subprocess, os

os.chdir(os.path.dirname(__file__))
timeLeft = 6
while timeLeft > 0:
    print(timeLeft, end='')
    time.sleep(1)
    timeLeft = timeLeft - 1

# At the end of the countdown, play a sound file.
subprocess.Popen(['start', 'alarm.wav'], shell=True)
