FROM python:3.11-slim

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir aiogram aiohttp asyncpg sqlalchemy python-dotenv requests

CMD ["python", "-m", "bot.main"]
