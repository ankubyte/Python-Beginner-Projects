
from user_agent import generate_user_agent
import requests,random,os
import json
from colorama import Fore,init
init(autoreset=True)
red=Fore.LIGHTRED_EX
yellow=Fore.LIGHTYELLOW_EX
green=Fore.LIGHTGREEN_EX
reset=Fore.RESET
mag=Fore.LIGHTMAGENTA_EX
cyan=Fore.LIGHTCYAN_EX

def quizes():
    data={}

    while True:

        url=f'https://opentdb.com/api.php?amount=1&category=18&difficulty=easy&type=multiple'

        head={
            "user-agent":generate_user_agent()
        }

        req=requests.get(url=url,headers=head,timeout=2)

        if req.status_code!=200:
            continue

        else:
            res=req.json()
            data['data']=res
            break

    return data

# print(quizes())

def obtain_ques():
    optt={}
    q=quizes()
    que=q['data']['results'][0]['question']
    c_opt= q['data']['results'][0]['correct_answer']
    n_opt= q['data']['results'][0]['incorrect_answers']
    a=['a','b','c','d']

    options=n_opt+[c_opt]
    random.shuffle(options )
    for x,y in zip(a,options):
        optt[x]=y
    return que,c_opt,optt



def main():
    os.system('cls' if os.name=='nt' else "clear")

    print(f'{red}Welcome To KBC\n{reset}')

    print(f"{yellow}Enter:{reset} a/b/c/d for respectative options\n")
    print(f'{green}Lets start\n{reset}')
    i=0
    while True:

        
        que,cor_opt,options=obtain_ques()

        i+=1


        print(f'{red}{i}) {que}{reset}')
        # print(options)
        # print(cor_opt)

        for x,y in options.items():
            print(f'{x} = {y}')

        ans=input(f"{reset}Enter opt or q to exit>> {green}").strip().lower()
        if ans=='q':
            print(f"Okay GoodByee")
            break
        else:

            user_ans=options[ans]
            print(f'{cyan}You Choose: {user_ans}')
            if user_ans==cor_opt:
                print(f"{green}You ans is Correct\n{reset}")
            else:
                print(f"{mag}Wrong Ans")

main()




