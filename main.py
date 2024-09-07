import requests as req
import concurrent.futures
import time

# i wont explain how to get your mm2 clash Autorization, just turn on your brain!
accounts = { # change
    "roblox_username": "mm2 clash Authorization", # robloxusername:Authorization
    "more_accounts": "mm2clash Authorization" 
    # more...
}

def send_message(account, token):
    headers = {
        "Authorization": token
    }
    payload = {
        "message": "your message!"
    }
    time.sleep(1)
    res = req.post("https://mm2clash.com/api/message", headers=headers, json=payload)
    if res.status_code == 200:
        return f"{account} success said!"
    else:
        return f"{account} failed say!"
      
print("made by leoidagoat on discord!")
while True:
    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(send_message, account, token) for account, token in accounts.items()]
        for future in concurrent.futures.as_completed(futures):
            print(future.result())
            time.sleep(1)
