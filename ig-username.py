import requests,json,random,string,os,sys
from threading import Thread

red = "\033[1m\033[31m"
green = "\033[1m\033[32m"
yellow = "\033[1m\033[33m"
blue = "\033[1m\033[34m"
cyan = "\033[1m\033[36m"
magenta = "\033[1m\033[35m"
M = "\033[1m\033[36m"
white = "\033[1m\033[37m"
orange = "\033[1m\033[38;5;208m"
reset = "\033[0m"

g_name=b_name=error=0
def status(uname):
    os.system('clear' if os.name != 'nt' else 'cls')
    output = (
        f"{green}✅ Good Name : {g_name}{reset}\n"
        f"{red}❌ Bad Name : {b_name}{reset}\n"
        f"{yellow}⚠️  Error : {error}{reset}\n"
        f"{blue}👤 Usernames : {white}{uname}{reset}\n\n"
        f"{magenta}💻 Code By: {cyan}@AnkuByte"
    )
    sys.stdout.write(output + "\n")
    sys.stdout.flush()

def checker(username):
    
    result=""
    lsd=''.join(random.choices(string.ascii_letters + string.digits, k=32))
    url=f'https://www.instagram.com/api/graphql'
    head={
  "x-fb-lsd": lsd,#"AdR-oXqfemwUIBnwSrMy2anRRoE",
  "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/148.0.0.0 Safari/537.36",
  "content-type": "application/x-www-form-urlencoded",
  "sec-ch-ua-platform-version": "\"10.0.0\"",
  "accept": "*/*",
  "origin": "https://www.instagram.com",
  "sec-fetch-site": "same-origin",
  "referer": "https://www.instagram.com/accounts/emailsignup/",
  "accept-language": "en-US,en;q=0.9",

    }
    variables = {
        "input": {
            "fetch_username_suggestions": True,
            "field_name": "USERNAME",
            "username": {
                "sensitive_string_value": username
            }   
        },
        "scale": 1
    }

    data ={

  "lsd": lsd,#"AdR-oXqfemwUIBnwSrMy2anRRoE",
  "jazoest": "22484",

  "__crn": "comet.igweb.PolarisCAAIGRegistrationHomepageRoute",
  "qpl_active_flow_ids": "516759801",
  "fb_api_caller_class": "RelayModern",
  "fb_api_req_friendly_name": "useCAARegistrationFieldValidationQuery",
  "server_timestamps": "true",
  "variables": json.dumps(variables),
  "doc_id": "26387190147557007",
    }
    res=requests.post(url=url,headers=head,data=data)
    resp=res.json()

    if res.status_code!=200:
        result=f'Error status code={res.status_code}'
    else:
        validation = resp["data"]["xfb_caa_registration_field_validation"]    
        if validation['status']=="SUCCESS":
            result="yes_avilable"
        else:
            result='not_avilable'

    return result
            
gen_uname=[]
def name_gen(length:int):
    while True:
        uname= ''.join(random.choice(string.ascii_lowercase) for i in range(length))

        if uname not in gen_uname:
            gen_uname.append(uname)
            return uname
        
token = input(f"{red}Telegram Bot Token: {yellow}").strip()

chat_Id = input(f"{red}Telegram chat-id:{yellow} ").strip()
while True:
    try:
        leng = int(input(f"{reset}Enter length of username: {green}").strip())

        if leng <= 4:
            print(f"{red}Error: Length must be greater or equal to  5{reset}")
            continue

        break 

    except ValueError:
        print(f"{red}Error: Please enter a valid number{reset}")


def tg_send(uname):
    msg = f"‼️*Got an Instagram Username*\n\n✅*Username:* `{uname}`\n\n"
    
    buttons = {
        "inline_keyboard": [
            [
                {"text": "Channel", "url": "https://t.me/AnkuByte"}
            ]
        ]
    }
    
    requests.get(
        f"https://api.telegram.org/bot{token}/sendMessage",
        params={
            "chat_id": chat_Id,
            "text": msg,
            "parse_mode": "Markdown",
            "reply_markup": json.dumps(buttons)
        }
    )

def huntter():
    global g_name,b_name,error
    
    while True:
        username=name_gen(leng)
        result=checker(username)
        status(username)

        if result.lower()=='not_avilable':  
            b_name+=1
            status(username)
        elif result.lower()=='yes_avilable':
            g_name+=1
            status(username)
            with open('username-found.txt','a',encoding='utf-8') as f:
                f.write(username+'\n')
            tg_send(username)
            
        else: 
            error+=1
            status(username)
for _ in range(5):
    Thread(target=huntter).start()