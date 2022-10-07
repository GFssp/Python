import time
from datetime import datetime
from colorama import init
from termcolor import colored

init()


# A razão para os segundos não passarem é por que a função só declarada uma vez antes de rodar
def displayTime(time=datetime.now()):
    print(time.strftime("%B %d, %Y %H:%M %S"))


print(colored("Help! Time won't pass!", 'red'))

for c in range(10):
    displayTime()
    time.sleep(1)
