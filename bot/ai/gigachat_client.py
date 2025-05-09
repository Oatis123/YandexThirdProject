import os
import aiohttp
from bot.ai.gigachat_token import get_token
import requests

GIGACHAT_URL = os.getenv("GIGACHAT_URL", "https://gigachat.devices.sberbank.ru/api/v1/chat/completions")

async def ask_gigachat(prompt: str) -> str:
    token = get_token()
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }
    data = {
        "model": "GigaChat",
        "messages": [
            {"role": "user", "content": prompt}
        ],
        "max_tokens": 512
    }
    async with aiohttp.ClientSession() as session:
        async with session.post(GIGACHAT_URL, headers=headers, json=data, ssl=False) as resp:
            resp_json = await resp.json()
            if resp.status != 200:
                err = resp_json.get('detail') or resp_json.get('message') or str(resp_json)
                raise Exception(f"GigaChat API error: {err}")
            if "choices" in resp_json and resp_json["choices"]:
                return resp_json["choices"][0]["message"]["content"].strip()
            raise Exception(f"Некорректный ответ от GigaChat: {resp_json}")

class GigaChatClient:
    def __init__(self, access_token: str, base_url: str = "https://gigachat.devices.sberbank.ru/api/v1/"):
        self.access_token = access_token
        self.base_url = base_url
        self.headers = {
            "Authorization": f"Bearer {self.access_token}",
            "Content-Type": "application/json"
        }

    def generate_text(self, prompt: str, model: str = "GigaChat", max_tokens: int = 1000) -> str:
        url = self.base_url + "chat/completions"
        payload = {
            "model": model,
            "messages": [
                {"role": "user", "content": prompt}
            ],
            "max_tokens": max_tokens
        }
        response = requests.post(url, json=payload, headers=self.headers)
        response.raise_for_status()
        data = response.json()
        return data["choices"][0]["message"]["content"].strip()
