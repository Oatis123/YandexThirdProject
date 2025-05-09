import os
import asyncio
import base64
import requests
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

GIGACHAT_AUTH_KEY = os.getenv("GIGACHAT_AUTH_KEY")  # Authorization key (Base64)
GIGACHAT_SCOPE = os.getenv("GIGACHAT_SCOPE", "GIGACHAT_API_PERS")
GIGACHAT_OAUTH_URL = os.getenv("GIGACHAT_OAUTH_URL", "https://ngw.devices.sberbank.ru:9443/api/v2/oauth")

_token = None

def get_token():
    return _token

def fetch_token_sync():
    url = GIGACHAT_OAUTH_URL
    headers = {
        "Content-Type": "application/x-www-form-urlencoded",
        "Accept": "application/json",
        "RqUID": "f6e70a7e-c02a-4438-9640-99bc452fd15f",  # любой UUID, можно заменить на динамический
        "Authorization": f"Basic {GIGACHAT_AUTH_KEY}"
    }
    data = {"scope": GIGACHAT_SCOPE}
    try:
        resp = requests.post(url, headers=headers, data=data, verify=False, timeout=10)
        print(f"[GigaChat] Ответ на запрос токена: {resp.text}")
        resp.raise_for_status()
        token = resp.json()["access_token"]
        print(f"[GigaChat] Получен токен: {token}")
        return token
    except Exception as e:
        print(f"[GigaChat] Ошибка получения токена: {e}")
        return None

async def update_token_loop():
    global _token
    while True:
        try:
            _token = fetch_token_sync()
            print("[GigaChat] Access token обновлён")
        except Exception as e:
            print(f"[GigaChat] Ошибка обновления токена: {e}")
        await asyncio.sleep(60 * 30)  # 30 минут

try:
    _token = fetch_token_sync()
except Exception as e:
    print(f"[GigaChat] Ошибка инициализации токена: {e}")
