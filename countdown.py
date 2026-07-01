import time,os
from colorama import Fore,init
cyan=Fore.LIGHTCYAN_EX
init(autoreset=True)
def live_CountDown():
    a=time.strftime("%I : %M : %S %p",time.localtime())
    b=f"{cyan}\r{a}"
    print(b,end="",flush=True)
    time.sleep(1)

os.system('cls')
while True:
    live_CountDown()