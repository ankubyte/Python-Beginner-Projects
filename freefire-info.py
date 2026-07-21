import requests,os
from colorama import Fore, Style, init

init(autoreset=True)
TITLE = Fore.CYAN + Style.BRIGHT
reset=Fore.RESET
LABEL = Fore.YELLOW
VALUE = Fore.GREEN
ERROR = Fore.RED + Style.BRIGHT
HEADER = Fore.MAGENTA + Style.BRIGHT
def test_get_command(98376389):
    INFO_API = "https://info.killersharmabot.online/player-info?uid={uid}"
    
    print(f"{LABEL}Fetching data for UID {uid}...{reset}\n")
    
    try:
        r = requests.get(INFO_API.format(uid=uid), timeout=30)
        data = r.json()

        b = data.get("basicInfo", {})
        s = data.get("socialInfo", {})
        p = data.get("profileInfo", {})
        pet = data.get("petInfo", {})
        clan = data.get("clanBasicInfo", {})
        captain = data.get("captainBasicInfo", {})
        credit = data.get("creditScoreInfo", {})

        text = f"""
{HEADER}══════════════════════════════════════════════════════
🔥              FREE FIRE PLAYER INFO
══════════════════════════════════════════════════════

{TITLE}┌─ BASIC INFORMATION
{LABEL}├─ 🕵️ Prime Level      : {VALUE}{b.get('primeLevel',{}).get('level','N/A')}
{LABEL}├─ 👤 Name             : {VALUE}{b.get('nickname','N/A')}
{LABEL}├─ 🆔 UID              : {VALUE}{b.get('accountId','N/A')}
{LABEL}├─ 🎮 Level            : {VALUE}{b.get('level','N/A')} ({b.get('exp','N/A')} EXP)
{LABEL}├─ 🌍 Region           : {VALUE}{b.get('region','N/A')}
{LABEL}├─ ❤️ Likes            : {VALUE}{b.get('liked','N/A')}
{LABEL}├─ 🚀 Honor Score      : {VALUE}{credit.get('creditScore','N/A')}
{LABEL}├─ 🏷️ Title            : {VALUE}{captain.get('titleName','Not Found')}
{LABEL}└─ 📝 Signature        : {VALUE}{s.get('signature','N/A')}

{TITLE}┌─ ACTIVITY INFORMATION
{LABEL}├─ 🔋 Version          : {VALUE}{b.get('releaseVersion','N/A')}
{LABEL}├─ 🎖️ BP Badges        : {VALUE}{b.get('badgeCnt','N/A')}
{LABEL}├─ 🏆 BR Rank          : {VALUE}{b.get('rankingName','N/A')}
{LABEL}├─ 🥇 CS Rank          : {VALUE}{b.get('csRankingName','N/A')}
{LABEL}├─ 🚻 Gender           : {VALUE}{s.get('gender','N/A')}
{LABEL}├─ 🎯 Rank Display     : {VALUE}{s.get('rankShow','N/A')}
{LABEL}├─ 📜 Show BR Rank     : {VALUE}{b.get('showBrRank','N/A')}
{LABEL}└─ 💢 Show CS Rank     : {VALUE}{b.get('showCsRank','N/A')}

{TITLE}┌─ PROFILE INFORMATION
{LABEL}├─ 🖼️ Avatar           : {VALUE}{p.get('avatarName','N/A')}
{LABEL}├─ 📢 Banner           : {VALUE}{b.get('bannerName','N/A')}
{LABEL}├─ 📌 Pin              : {VALUE}{b.get('pinName','N/A')}
{LABEL}├─ 🥽 Skills           : {VALUE}{p.get('equippedSkillsNames','N/A')}
{LABEL}├─ 🌐 Language         : {VALUE}{s.get('language','N/A')}
{LABEL}├─ 🔫 Equipped Gun     : {VALUE}{b.get('equippedGunName','N/A')}
{LABEL}└─ ✨ Animation        : {VALUE}{b.get('equippedAnimationName','N/A')}

{TITLE}┌─ PET DETAILS
{LABEL}├─ 🐶 Pet Name         : {VALUE}{pet.get('petName','N/A')}
{LABEL}├─ 🎨 Pet Skin         : {VALUE}{pet.get('skinName','N/A')}
{LABEL}├─ 🧬 Pet EXP          : {VALUE}{pet.get('exp','N/A')}
{LABEL}└─ 🎴 Pet Level        : {VALUE}{pet.get('level','N/A')}

{TITLE}┌─ GUILD INFORMATION
{LABEL}├─ 🏷️ Guild Name       : {VALUE}{clan.get('clanName','Not Found')}
{LABEL}├─ 🆔 Guild ID         : {VALUE}{clan.get('clanId','Not Found')}
{LABEL}├─ ⭐ Guild Level      : {VALUE}{clan.get('clanLevel','Not Found')}
{LABEL}├─ 👥 Members          : {VALUE}{clan.get('memberNum','Not Found')}
{LABEL}└─ 👑 Leader           : {VALUE}{captain.get('nickname','Not Found')}

{HEADER}══════════════════════════════════════════════════════
"""
        print(text)

    except requests.exceptions.RequestException as e:
        print(f"❌ Network or API Error: {e}")
    except Exception as e:
        print(f"❌ Error parsing data: {e}")

if __name__ == "__main__":
    print(f'{Fore.LIGHTMAGENTA_EX}Welcome To Free fire profile analyzer')
    target_uid = input(f"{Fore.LIGHTRED_EX}Enter a Free Fire UID to test: {reset}").strip()
    os.system('cls' if os.name=='nt' else 'clear')
    if target_uid:
        test_get_command(target_uid)
    else:
        print("No UID provided.")

