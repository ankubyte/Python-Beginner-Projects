import groq,os
red = "\033[1m\033[31m" 
green = "\033[1m\033[32m"
yellow = "\033[1m\033[33m"
reset = "\033[0m"
cyan = "\033[1m\033[36m"
magenta = "\033[1m\033[35m" 
print(f"If u Dont have Api get it from Groq official site")
token=input(f'{yellow}Enter APi Token: {reset}').strip()
client=groq.Groq(api_key=token)

def Ai_chat(text:str):
    chat_comp=client.chat.completions.create(
        messages=[
           { 'role':'system','content': "Heyy you are Divya an Intelligent female Ai robot created by Sir Ankush and his social media handle is: @AnkuByte,hee is very intelligent,pl send respone polietly and lovely way"},
           {"role":'user',"content":text}
        ],
        model='openai/gpt-oss-120b',
 
    )
    Ai_reply=chat_comp.choices[0].message.content
    return Ai_reply

def main():
    print(f"{yellow}Welcome to Ai-Gpt\n{reset}{red}By{reset}=:{reset}{green} @AnkuByte\n")
    print(f'{reset}='*100)
    print(f'{red}Enter text or q to exit...')
    while True:
        
        text=input(f'{magenta}user>>> {reset}').strip()
        if text.lower()=='q':
            print(f'{red}thank for using,okay byeee')
            break
        else:
            aii=Ai_chat(text)
            print(f'{yellow}Ai say>>> {reset}{aii}')
            continue

main()