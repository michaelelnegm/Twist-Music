import json
import time
import requests
from colorama import Fore, Style, init
init(autoreset=True)
def display_hub():
    print(Fore.CYAN + "=======================================================")
    print(Fore.MAGENTA + Style.BRIGHT + "          TWIST MUSIC LOYALTY MULTI-TOOL          ")
    print(Fore.GREEN + "  [+] Telegram Channel : https://t.me/ElnegmDev")
    print(Fore.YELLOW + "  [+] GitHub           : https://github.com/michaelelnegm")
    print(Fore.GREEN + "  [+] Developer        : @ebn_elnegm")
    print(Fore.CYAN + "=======================================================\n")

display_hub()

print(Fore.CYAN + " [1] " + Fore.WHITE + "تجميع النقاط (Auto-Claim Actions)")
print(Fore.CYAN + " [2] " + Fore.WHITE + "استبدال المكافآت (Redeem Packages)")
print(Fore.CYAN + "-------------------------------------------------------")

try:
    operation_mode = int(input(Fore.YELLOW + " [?] اختر العملية (1 أو 2): " + Fore.WHITE))
    if operation_mode not in [1, 2]:
        print(Fore.RED + " [-] Invalid operation mode selected. Exiting...")
        exit()
except ValueError:
    print(Fore.RED + " [-] Numeric value required.")
    exit()

msisdn = input(Fore.YELLOW + "\n [?] Enter Number (010xxxxxxx): " + Fore.WHITE)
request_otp_url = "https://api.twistmena.com/music/Dlogin/sendCode"
otp_payload = {"dial": f"2{msisdn}"}

session_headers = {
    "User-Agent": "Twist-Mobile/11.2.10 (Android; 12; V2550; music; ar-EG)",
    "Accept": "application/json",
    "Accept-Encoding": "gzip",
    "Content-Type": "application/json",
    "tgdeviceid": "26716333",
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
    "sessionid": "dbe825c7-a965-4b59-8b0d-e7f60252f9e9",
}

print(Fore.BLUE + " [*] Dispatching OTP challenge...")
otp_req = requests.post(request_otp_url, data=json.dumps(otp_payload), headers=session_headers)

if "SUCCESS" in otp_req.text:
    print(Fore.GREEN + " [+] OTP challenge sent successfully.")
else:
    print(Fore.RED + f" [-] Transmission error: {otp_req.text}")
    exit()

otp_token = input(Fore.YELLOW + "\n [?] Enter OTP Code: " + Fore.WHITE)
verify_otp_url = "https://api.twistmena.com/music/Dlogin/verify"
verification_payload = {
    "dial": f"2{msisdn}",
    "verifyCode": otp_token,
    "socialServiceName": "",
    "socialServiceToken": "",
}

print(Fore.BLUE + " [*] Validating credentials...")
auth_req = requests.post(verify_otp_url, data=json.dumps(verification_payload), headers=session_headers)

if "token" not in auth_req.text:
    print(Fore.RED + f" [-] Authentication checkpoint failed: {auth_req.text}")
    exit()

print(Fore.GREEN + " [+] Authentication verified.")

session_metadata = auth_req.json()
jwt_token = session_metadata.get("token")
api_access_token = session_metadata.get("accessToken")
telecom_tg_token = session_metadata.get("tgToken")
telecom_refresh_token = session_metadata.get("tgRefreshToken")

session_headers["authorization"] = f"Bearer {jwt_token}"
session_headers["access-token"] = api_access_token
session_headers["tg-token"] = telecom_tg_token
session_headers["tg-refresh-token"] = telecom_refresh_token

balance_endpoint = "https://api.twistmena.com/music/user/loyalty/balance/details"
print(Fore.BLUE + " [*] Retrieving ledger details...")
try:
    balance_req = requests.get(balance_endpoint, headers=session_headers)
    wallet_balance = balance_req.json().get("balance", 0)
    print(Fore.MAGENTA + Style.BRIGHT + f" [$] Current Ledger Balance: {wallet_balance} Coins \n")
except Exception:
    wallet_balance = "Unknown"
    print(Fore.RED + " [!] Failed to balance check account context.")

if operation_mode == 1:
    action_matrix = [
        "SIGNUP", "UPGRADE_TO_PREMIUM", "LIBRARY_IMPORT", "FIRST_STREAM_OF_THE_DAY",
        "LIKE_SONG", "SHARE_SONG", "DOWNLOAD_SONG", "ADD_TO_PLAYLIST",
        "SHARE_PLAYLIST", "FIRST_PODCAST_OF_THE_DAY", "FIRST_RADIO_OF_THE_DAY",
        "FIRST_TWIST_LIVE_RADIO_OF_THE_DAY", "QURAN_RADIO", "FIRST_AUDIOBOOK_OF_THE_DAY",
        "WATCH_VIDEO", "SUCCESSFUL_CHARGE", "CREATE_PLAYLIST", "CHOSE_FAVORITE_ARTISTS",
        "ARTIST_FAN_STREAMING", "ECHO_SONG", "DAILY_CHECKIN", "STREAM_SONG"
    ]

    print(Fore.CYAN + "=======================================================")
    print(Fore.CYAN + " >>> Initializing routine automation loop...")
    print(Fore.CYAN + "=======================================================")

    session_headers["content-length"] = "0"

    for action_node in action_matrix:
        action_target_url = f"https://api.twistmena.com/music/loyalty/action/{action_node}"
        print(Fore.WHITE + " -> Processing: " + Fore.YELLOW + f"{action_node:<35}" + Fore.WHITE + " -> ", end="")
        
        try:
            execution_res = requests.post(action_target_url, headers=session_headers)
            if execution_res.status_code in [200, 201]:
                print(Fore.GREEN + f"OK [{execution_res.status_code}]")
            else:
                print(Fore.RED + f"FAIL [{execution_res.status_code}]")
            print(Fore.LIGHTBLACK_EX + f"    | Raw Payload: {execution_res.text.strip()}")
        except Exception as api_err:
            print(Fore.RED + f"EXC_ERR: {api_err}")
            
        print(Fore.CYAN + "-------------------------------------------------------")
        time.sleep(1)

    print(Fore.GREEN + Style.BRIGHT + "\n [+] Pipeline tasks executed successfully!")

elif operation_mode == 2:
    catalog_endpoint = "https://api.twistmena.com/music/user/loyalty/packages"
    
    print(Fore.BLUE + " [*] Querying internal reward catalogs...")
    try:
        catalog_req = requests.get(catalog_endpoint, headers=session_headers)
        catalog_payload = catalog_req.json()
    except Exception as data_err:
        print(Fore.RED + f" [-] Parsing routine failure: {data_err}")
        exit()

    extracted_packages = []
    for node_segment in catalog_payload.get("packages", {}).values():
        for product_node in node_segment:
            if "id" in product_node:
                extracted_packages.append({
                    "id": product_node["id"],
                    "name": product_node.get("name", "Unnamed Item"),
                    "cost": product_node.get("cost", 0),
                    "available": product_node.get("available", True)
                })

    print(Fore.CYAN + "\n=================== المتاح حالياً ===================")
    for index_key, product in enumerate(extracted_packages):
        availability_flag = Fore.GREEN + "متاح" if product["available"] else Fore.RED + "غير متاح"
        print(f" {Fore.CYAN}[{index_key}]{Fore.WHITE} {product['name']:<25} | التكلفة: {product['cost']:<5} كوينز | الحالة: {availability_flag}")
    print(Fore.CYAN + "=======================================================")

    try:
        selection_idx = int(input(Fore.YELLOW + " [?] أدخل رقم الخدمة التي تريد استبدالها: " + Fore.WHITE))
        if selection_idx < 0 or selection_idx >= len(extracted_packages):
            print(Fore.RED + " [-] Out of bounds selection index. Terminating...")
            exit()
    except ValueError:
        print(Fore.RED + " [-] Integer parse failed.")
        exit()

    targeted_package = extracted_packages[selection_idx]
    
    if isinstance(wallet_balance, int) and wallet_balance < targeted_package["cost"]:
        print(Fore.YELLOW + f" [!] Warning: Wallet balance ({wallet_balance}) is less than item cost ({targeted_package['cost']}).")
        user_override = input(Fore.YELLOW + " [?] Force action execution anyway? (y/n): " + Fore.WHITE).lower()
        if user_override != 'y':
            print(Fore.RED + " [-] Session aborted by user.")
            exit()

    print(Fore.BLUE + f"\n [*] Transmitting settlement request for: {targeted_package['name']} ({targeted_package['id']})...")
    
    settlement_url = f"https://api.twistmena.com/music/loyalty/redeem/{targeted_package['id']}"
    session_headers["content-length"] = "0"

    try:
        settlement_res = requests.post(settlement_url, headers=session_headers)
        print(Fore.CYAN + "\n--- نتيجة التفعيل (Response) ---")
        if settlement_res.status_code in [200, 201]:
            print(Fore.GREEN + f" [+] Operation status code: {settlement_res.status_code} (Success)")
        else:
            print(Fore.RED + f" [-] Operation status code: {settlement_res.status_code} (Rejected)")
        print(Fore.WHITE + settlement_res.text.strip())
    except Exception as runtime_err:
        print(Fore.RED + f" [-] Runtime network crash during exchange process: {runtime_err}")
