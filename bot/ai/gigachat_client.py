import os
import aiohttp
import requests

GIGACHAT_TOKEN = os.getenv("GIGACHAT_TOKEN")
GIGACHAT_URL = os.getenv("GIGACHAT_URL", "https://gigachat.devices.sberbank.ru/api/v1/chat/completions")

async def ask_gigachat(prompt: str) -> str:
    headers = {
        "Authorization": f"Bearer {GIGACHAT_TOKEN}",
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
        async with session.post(GIGACHAT_URL, headers=headers, json=data) as resp:
            resp_json = await resp.json()
            return resp_json["choices"][0]["message"]["content"].strip()

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
