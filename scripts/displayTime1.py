import time
from datetime import datetime
from colorama import init
from termcolor import colored

init()


def displayTime(time=None):
    if time is None:
        time = datetime.now()
    print(time.strftime("%B %d, %Y %H:%M %S"))


print(colored('YES! Now the time is passing!', 'green'))

for c in range(10):
    displayTime()
    time.sleep(1)
