import json
import time
import requests
from colorama import Fore, Style, init

init(autoreset=True)

def print_banner():
    print(Fore.CYAN + "=======================================================")
    print(Fore.MAGENTA + Style.BRIGHT + "          TWIST MUSIC LOYALTY AUTO-CLAIMER          ")
    print(Fore.GREEN + "  [+] Telegram Channel : https://t.me/ElnegmDev")
    print(Fore.YELLOW + "  [+] GitHub : https://github.com/michaelelnegm")
    print(Fore.GREEN + "  [+] Developer        : @ebn_elnegm")
    print(Fore.CYAN + "=======================================================\n")

print_banner()

nu = input(Fore.YELLOW + " [?] Enter Number (010xxxxxxx): " + Fore.WHITE)
url1 = "https://api.twistmena.com/music/Dlogin/sendCode"

payload1 = {"dial": f"2{nu}"}

headers1 = {
    "User-Agent": "Twist-Mobile/11.2.10 (Android; 12; V2550; music; ar-EG)",
    "Accept": "application/json",
    "Accept-Encoding": "gzip",
    "Content-Type": "application/json",
    "tgdeviceid": "",
    "app_version": "11.2.10",
    "device_token": "",
    "appversion": "11.2.10",
    "channel": "mobileapp",
    "access-token": "",
    "platform": "android",
    "tg-token": "",
    "accept-language": "ar",
    "tg-refresh-token": "",
    "device_id": "BP2A.250605.031.A3_V000L1",
    "sessionid": "14632a72-57b5-48a8-8960-a82d5cbc9d24",
}

print(Fore.BLUE + "\n [*] Sending OTP...")
response1 = requests.post(url1, data=json.dumps(payload1), headers=headers1)

if "SUCCESS" in response1.text:
    print(Fore.GREEN + " [+] OTP sent.")
else:
    print(Fore.RED + f" [-] Error: {response1.text}")
    exit()

co = input(Fore.YELLOW + "\n [?] Enter OTP Code: " + Fore.WHITE)

url2 = "https://api.twistmena.com/music/Dlogin/verify"

payload2 = {
    "dial": f"2{nu}",
    "verifyCode": co,
    "socialServiceName": "",
    "socialServiceToken": "",
}

headers2 = headers1  

print(Fore.BLUE + " [*] Verifying...")
response2 = requests.post(url2, data=json.dumps(payload2), headers=headers2)

if "token" in response2.text:
    print(Fore.GREEN + " [+] Auth success.")
else:
    print(Fore.RED + f" [-] Auth failed: {response2.text}")
    exit()

data = response2.json()
token = data.get("token")
access_token = data.get("accessToken")
tg_token = data.get("tgToken")
tg_refreshtoken = data.get("tgRefreshToken")

url3 = "https://api.twistmena.com/music/user/loyalty/balance/details"
headers3 = {
    "User-Agent": "Twist-Mobile/11.2.10 (Android; 12; V2550; music; ar-EG)",
    "Accept": "application/json",
    "Accept-Encoding": "gzip",
    "tgdeviceid": "26716333",
    "app_version": "11.2.10",
    "device_token": "",
    "appversion": "11.2.10",
    "channel": "mobileapp",
    "authorization": f"Bearer {token}",
    "content-type": "application/json",
    "access-token": access_token,
    "platform": "android",
    "tg-token": tg_token,
    "accept-language": "ar",
    "tg-refresh-token": tg_refreshtoken,
    "device_id": "BP2A.250605.031.A3_V000L1",
    "sessionid": "a9abe49c-85dc-4914-b705-8834349191c1",
}

print(Fore.BLUE + " [*] Fetching balance...")
try:
    response3 = requests.get(url3, headers=headers3)
    blance = response3.json().get("balance", 0)
    print(
        Fore.MAGENTA
        + Style.BRIGHT
        + f" [$] Balance: {blance} Coins \n"
    )
except Exception:
    blance = "Unknown"
    print(Fore.RED + " [!] Failed to get balance.")

ids_list = [
    "SIGNUP",
    "UPGRADE_TO_PREMIUM",
    "LIBRARY_IMPORT",
    "FIRST_STREAM_OF_THE_DAY",
    "LIKE_SONG",
    "SHARE_SONG",
    "DOWNLOAD_SONG",
    "ADD_TO_PLAYLIST",
    "SHARE_PLAYLIST",
    "FIRST_PODCAST_OF_THE_DAY",
    "FIRST_RADIO_OF_THE_DAY",
    "FIRST_TWIST_LIVE_RADIO_OF_THE_DAY",
    "QURAN_RADIO",
    "FIRST_AUDIOBOOK_OF_THE_DAY",
    "WATCH_VIDEO",
    "SUCCESSFUL_CHARGE",
    "CREATE_PLAYLIST",
    "CHOSE_FAVORITE_ARTISTS",
    "ARTIST_FAN_STREAMING",
    "ECHO_SONG",
    "DAILY_CHECKIN",
    "STREAM_SONG",
]

headers_claim = {
    "User-Agent": "Twist-Mobile/11.2.10 (Android; 12; V2550; music; ar-EG)",
    "Accept": "application/json",
    "Accept-Encoding": "gzip",
    "tgdeviceid": "24138176",
    "app_version": "11.2.10",
    "device_token": "",
    "appversion": "11.2.10",
    "channel": "mobileapp",
    "authorization": f"Bearer {token}",
    "content-type": "application/json",
    "access-token": access_token,
    "platform": "android",
    "tg-token": tg_token,
    "accept-language": "ar",
    "content-length": "0",
    "tg-refresh-token": tg_refreshtoken,
    "device_id": "BP2A.250605.031.A3_V000L1",
    "sessionid": "3cc42fcd-a4f6-45c7-81ae-ec82f3b7c0b6",
}

print(Fore.CYAN + "=======================================================")
print(Fore.CYAN + " >>> Running actions loop...")
print(Fore.CYAN + "=======================================================")

for m in ids_list:
    url = f"https://api.twistmena.com/music/loyalty/action/{m}"

    print(
        Fore.WHITE
        + f" -> Action: "
        + Fore.YELLOW
        + f"{m:<35}"
        + Fore.WHITE
        + " -> ",
        end="",
    )

    try:
        response = requests.post(url, headers=headers_claim)

        if response.status_code == 200 or response.status_code == 201:
            print(Fore.GREEN + f"OK [{response.status_code}]")
        else:
            print(Fore.RED + f"FAIL [{response.status_code}]")

        print(Fore.LIGHTBLACK_EX + f"    | Response: {response.text.strip()}")

    except Exception as e:
        print(Fore.RED + f"ERROR: {e}")

    print(Fore.CYAN + "-------------------------------------------------------")
    time.sleep(1)

print(Fore.GREEN + Style.BRIGHT + "\n [+] All tasks done!")
