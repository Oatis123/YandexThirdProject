import os
import aiohttp
from typing import Optional
from langchain_ollama import OllamaLLM
import asyncio

OLLAMA_URL = os.getenv("OLLAMA_URL", "http://localhost:11434")
DEFAULT_QWEN_MODEL = os.getenv("QWEN_MODEL", "qwen2.5:1.5b")

async def ask_qwen(prompt: str, model: Optional[str] = None) -> str:
    model = model or DEFAULT_QWEN_MODEL
    llm = OllamaLLM(base_url=OLLAMA_URL, model=model)
    loop = asyncio.get_event_loop()
    # Langchain Ollama LLM работает синхронно, оборачиваем в executor
    return await loop.run_in_executor(None, llm.invoke, prompt)

class QwenOllamaClient:
    def __init__(self, base_url: str = None):
        self.base_url = base_url or OLLAMA_URL

    async def generate_text(self, prompt: str, model: str = None) -> str:
        return await ask_qwen(prompt, model)
