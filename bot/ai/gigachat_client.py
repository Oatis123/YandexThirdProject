import requests

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
