import os
import asyncio
import base64
import requests

GIGACHAT_AUTH_KEY = os.getenv("GIGACHAT_AUTH_KEY")  # Authorization key (Base64)
GIGACHAT_SCOPE = os.getenv("GIGACHAT_SCOPE", "GIGACHAT_API_PERS")
GIGACHAT_OAUTH_URL = os.getenv("GIGACHAT_OAUTH_URL", "https://ngw.devices.sberbank.ru:9443/api/v2/oauth")

_token = None

def get_token():
    return _token

def fetch_token_sync():
    headers = {
        "Content-Type": "application/x-www-form-urlencoded",
        "Accept": "application/json",
        "RqUID": "token-req-12345",  # Можно сгенерировать uuid
        "Authorization": f"Basic {GIGACHAT_AUTH_KEY}"
    }
    data = {"scope": GIGACHAT_SCOPE}
    resp = requests.post(GIGACHAT_OAUTH_URL, headers=headers, data=data, verify=False)
    resp.raise_for_status()
    return resp.json()["access_token"]

async def update_token_loop():
    global _token
    while True:
        try:
            _token = fetch_token_sync()
            print("[GigaChat] Access token обновлён")
        except Exception as e:
            print(f"[GigaChat] Ошибка обновления токена: {e}")
        await asyncio.sleep(60 * 30)  # 30 минут
