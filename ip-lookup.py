import requests,json

red = "\033[1m\033[31m" 
green = "\033[1m\033[32m"
yellow = "\033[1m\033[33m"
reset = "\033[0m"

print(f'{yellow}Code By @AnkuByte')
def ipCheck(choice:str):
    information={}
    if choice.lower()=='1' or '':
        res=requests.get(f"http://ip-api.com/json/", timeout=5).json()  
        query=res['query']
        
        information = {
            "message": f"Here is your IP info: {query}",
            "data": res
        }
    else:
        url=f"http://ip-api.com/json/{choice}"
        head={
    "user-agent": "Mozilla/5.0 (Linux; Android 15; Pixel 9) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/149.0.0.0 Mobile Safari/537.36",
        }
        
        res=requests.get(url=url,headers=head,timeout=5).json()
        query=res['query']

        information = {
            "message": f"Here is your IP info: {query}",
            "data": res
        }
    return information


def result():
    print(f'{red}Please Enter any Ip address to check or type 1 to check ur info{reset} ')
    choice=input(f'{reset}Enter 1 or Ip: {green}').strip()
    res=ipCheck(choice)
    print(f"{green}Here is Ip info: {yellow}")
    print(reset)
    res_json=json.dumps(res,indent=2)
    print(res_json)
result()

#ankubyte.t.me