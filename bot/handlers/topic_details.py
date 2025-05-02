from aiogram import Router
from aiogram.types import Message

router = Router()

TOPIC_DETAILS = {
    1: {
        "short": "Переменные, условия, циклы, функции, классы — это основы Python.\nПример:\n\nfor i in range(3):\n    print(i)",
        "long": "В Python переменные не требуют объявления типа.\nУсловия: if, elif, else.\nЦиклы: for, while.\nФункции: def имя(...): ...\nКлассы: class Имя: ...\n\nПример функции:\ndef add(a, b):\n    return a + b\n\nПодробнее: https://docs.python.org/3/tutorial/"
    },
    2: {
        "short": "Сортировки, поиск, рекурсия, жадные алгоритмы — базовые алгоритмы.\nПример сортировки:\narr = [3,1,2]\narr.sort()",
        "long": "Сортировки: пузырьком, быстрая, вставками и др.\nПоиск: линейный, бинарный.\nРекурсия — вызов функции самой себя.\nЖадные алгоритмы — локально оптимальный выбор.\n\nПример рекурсии:\ndef fact(n):\n    return 1 if n==0 else n*fact(n-1)\n\nПодробнее: https://ru.wikipedia.org/wiki/Алгоритм"
    },
    3: {
        "short": "Стек, очередь, дерево, граф — основные структуры данных.\nПример стека:\nstack = []\nstack.append(1)\nstack.pop()",
        "long": "Стек — LIFO, очередь — FIFO.\nДерево — иерархия, граф — связи между объектами.\n\nПример очереди:\nfrom collections import deque\nq = deque()\nq.append(1)\nq.popleft()\n\nПодробнее: https://ru.wikipedia.org/wiki/Структура_данных"
    }
}

@router.message()
async def topic_details(msg: Message):
    text = msg.text.strip()
    if text.isdigit():
        num = int(text)
        if num in TOPIC_DETAILS:
            short = TOPIC_DETAILS[num]["short"]
            await msg.answer(f"{short}\n\nНапишите 'Подробнее' для расширенного объяснения.")
            return
    if text.lower() == "подробнее":
        # Здесь можно хранить в БД последний выбранный топик пользователя, пока просто пример для 1-й темы
        await msg.answer(TOPIC_DETAILS[1]["long"])
        return
    await msg.answer("Для подробного объяснения выберите тему из списка /topics и напишите её номер.")
