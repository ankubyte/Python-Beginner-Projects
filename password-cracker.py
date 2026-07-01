import random,string,os
 
from colorama import Fore
red=Fore.LIGHTRED_EX
yellow=Fore.LIGHTYELLOW_EX
green=Fore.LIGHTGREEN_EX
reset=Fore.RESET
mag=Fore.LIGHTMAGENTA_EX
cyan=Fore.LIGHTCYAN_EX

def password():
    passw=''
    input_pass=int(input(f"{red}Enter 4 digit Num:{reset} ")) 
    passw=input_pass
    # print(passw)
    i=0
    while True:
        i+=1
        passww = ''.join(str(random.randint(0, 9)) for x in range(4))
        if int(passww)==int(passw):
            print(f'{reset}{i}) {reset}{green}Pass Found: {passww}{reset}')
            break
        else:
            print(f'{reset}{i}) {reset}{red}Searching...: {passww}{reset}')
            os.system('cls||clear')
            continue


password()