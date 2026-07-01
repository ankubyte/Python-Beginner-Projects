import base64,zlib,time,pathlib,os

from colorama import Fore, Style, init

init(autoreset=True)

RESET = Style.RESET_ALL
BOLD = Style.BRIGHT
RED = Fore.RED
GREEN = Fore.GREEN
YELLOW = Fore.YELLOW
BLUE = Fore.BLUE
MAGENTA = Fore.MAGENTA
CYAN = Fore.CYAN
GRAY = Fore.LIGHTBLACK_EX


def encryption(file:str):

    timestr=time.time()

    act_file=file

    with open(act_file,'r',encoding='utf-8') as f:
        code=f.read()

    byte_code=code.encode()

    obf1=base64.b64encode(byte_code)

    obf2=base64.b85encode(obf1)

    obf3=zlib.compress(obf2)

    rev=obf3[::-1]

    obf4=base64.b32encode(rev)

    enc = obf4.decode()

    timend=time.time()

    content = (

        f"#Code By @AnkuByte\n#Time Taken: {timend-timestr:.4f} sec\n"
        "_=lambda __:"
        "__import__('base64').b64decode("
        "__import__('base64').b85decode("
        "__import__('zlib').decompress("
        "__import__('base64').b32decode(__)[::-1]"
        ")));"
        "exec(_('%s'))"
    ) % enc

    try:

        ex_path=act_file.with_name(f"Enc_{act_file.name}")

        with open(ex_path,'w',encoding='utf-8') as f:
            f.write(content)

        print(f'{GREEN}Code successfully obfuscated,and saved as {ex_path}{RESET}')

    except Exception as err:
        print(f'{RED}Unknown Error: {RESET}{err}')


def main():
    os.system('cls' if os.name=="nt" else 'clear')
    print(f'{RED}Welcome To Python code Encryptor')

    file=pathlib.Path(input(f'{MAGENTA}Enter File Path:{RESET} ').strip())
    print(f'''
file Name: {file.name}
file size: {os.path.getsize(file)} kb
    ''')

    encryption(file)
main()
