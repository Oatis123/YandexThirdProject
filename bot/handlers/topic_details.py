from aiogram import Router
from aiogram.types import Message
from bot.keyboards.main import details_kb, topics_kb, main_menu_kb
from bot.ai.gigachat_client import ask_gigachat
from aiogram.utils.markdown import hbold, hcode

router = Router()

TOPIC_DETAILS = {
    1: {
        "short": (
            "Переменные, условия, циклы, функции, классы — это основы Python.\n"
            "\n"
            "Переменные позволяют хранить данные разных типов.\n"
            "Условия (if/elif/else) позволяют выполнять код в зависимости от логики.\n"
            "Циклы (for, while) нужны для повторения действий.\n"
            "Функции (def) — для структурирования и переиспользования кода.\n"
            "Классы (class) — для ООП и создания собственных типов данных.\n"
            "\n"
            "Пример цикла:\nfor i in range(3):\n    print(i)\n"
        ),
        "long": (
            "В Python переменные не требуют объявления типа, их можно переопределять.\n"
            "Условия: if, elif, else — позволяют реализовать ветвления.\n"
            "Циклы: for (по коллекциям/диапазону), while (пока условие истинно).\n"
            "Функции: def имя(...): ... — позволяют выносить повторяющийся код.\n"
            "Классы: class Имя: ... — основа ООП, инкапсуляция, наследование, полиморфизм.\n"
            "\n"
            "Пример функции:\ndef add(a, b):\n    return a + b\n"
            "\nПодробнее: https://docs.python.org/3/tutorial/"
        )
    },
    2: {
        "short": (
            "Сортировки, поиск, рекурсия, жадные алгоритмы — базовые алгоритмы.\n"
            "\n"
            "Сортировки позволяют упорядочить данные (например, sort, sorted).\n"
            "Поиск — нахождение элемента (линейный, бинарный).\n"
            "Рекурсия — функция вызывает саму себя для решения задачи.\n"
            "Жадные алгоритмы — принимают локально оптимальные решения на каждом шаге.\n"
            "\n"
            "Пример сортировки:\narr = [3,1,2]\narr.sort()\n"
        ),
        "long": (
            "Сортировки бывают простые (пузырьком, вставками) и быстрые (быстрая сортировка, слиянием).\n"
            "Поиск: линейный — перебор всех элементов, бинарный — деление пополам (только для отсортированных).\n"
            "Рекурсия — мощный инструмент, но требует аккуратности (условие выхода).\n"
            "Жадные алгоритмы часто используются для оптимизации, но не всегда дают глобальный оптимум.\n"
            "\n"
            "Пример рекурсии:\ndef fact(n):\n    return 1 if n==0 else n*fact(n-1)\n"
            "\nПодробнее: https://ru.wikipedia.org/wiki/Алгоритм"
        )
    },
    3: {
        "short": (
            "Стек, очередь, дерево, граф — основные структуры данных.\n"
            "\n"
            "Стек (LIFO) — последний вошёл, первый вышел.\n"
            "Очередь (FIFO) — первый вошёл, первый вышел.\n"
            "Дерево — иерархическая структура (например, дерево файлов).\n"
            "Граф — множество вершин и рёбер, описывает связи.\n"
            "\n"
            "Пример стека:\nstack = []\nstack.append(1)\nstack.pop()\n"
        ),
        "long": (
            "Стек реализуется через list, поддерживает push/pop. Используется для рекурсии, обхода деревьев.\n"
            "Очередь — через collections.deque, поддерживает append/popleft. Применяется в BFS, обработке событий.\n"
            "Дерево — структура с корнем и потомками, примеры: бинарное дерево поиска, дерево разбора выражений.\n"
            "Граф — универсальная структура для моделирования сетей, маршрутов, социальных связей.\n"
            "\n"
            "Пример очереди:\nfrom collections import deque\nq = deque()\nq.append(1)\nq.popleft()\n"
            "\nПодробнее: https://ru.wikipedia.org/wiki/Структура_данных"
        )
    }
}

def escape_markdown(text: str) -> str:
    escape_chars = r'_*[]()~`>#+-=|{}.!'
    return ''.join(f'\\{c}' if c in escape_chars else c for c in text)

@router.message(lambda m: m.text and m.text.startswith("1. "))
async def topic1(msg: Message):
    text = (
        "1. Переменные в Python:\n"
        "Переменные — это именованные области памяти, где можно временно хранить значения различных типов данных.\n"
        "В Python переменным не нужно объявлять тип заранее, он определяется автоматически при присваивании.\n\n"
        "x = 5   # Переменная x хранит целое число\n"
        "y = 'Hello'  # Переменная y хранит строку\n"
        "z = True  # Переменная z хранит булево значение (True или False)\n\n"
        "Пример:\n"
        "x = 5\nprint(x)  # Выведет 5"
    )
    await msg.answer(text, reply_markup=details_kb)

@router.message(lambda m: m.text and m.text.startswith("2. "))
async def topic2(msg: Message):
    text = (
        "2. Условия (if/elif/else):\n"
        "Инструкция if используется для выполнения блока кода только при выполнении условия.\n"
        "elif — дополнительная проверка, else — если ни одно условие не выполнено.\n\n"
        "x = 5\nif x > 0:\n    print('x больше нуля')\nelif x == 0:\n    print('x равно нулю')\nelse:\n    print('x меньше нуля')\n\n"
        "В этом примере, если x больше нуля, программа выведет сообщение 'x больше нуля'."
    )
    await msg.answer(text, reply_markup=details_kb)

@router.message(lambda m: m.text and m.text.startswith("3. "))
async def topic3(msg: Message):
    text = (
        "3. Циклы (for, while):\n"
        "Циклы используются для многократного выполнения кода.\n"
        "for — для перебора элементов коллекции, while — пока условие истинно.\n\n"
        "Цикл for:\n"
        "numbers = [1, 2, 3]\nfor num in numbers:\n    print(num)\n\n"
        "Цикл while:\n"
        "count = 0\nwhile count < 3:\n    print(count)\n    count += 1"
    )
    await msg.answer(text, reply_markup=details_kb)

@router.message(lambda m: m.text == "Подробнее")
async def details(msg: Message):
    prev = msg.reply_to_message.text if msg.reply_to_message else ""
    topic_num = 1
    if "алгоритм" in prev.lower():
        topic_num = 2
    elif "структур" in prev.lower():
        topic_num = 3
    user_prompt = f"Объясни подробно для новичка: {TOPIC_DETAILS[topic_num]['short']}. Не используй markdown, просто текстовое объяснение с примерами кода как в обычном чате>"
    try:
        ai_explanation = await ask_gigachat(user_prompt)
        ai_explanation = ai_explanation.translate(str.maketrans("", "", "#`*"))
        doc = TOPIC_DETAILS[topic_num]["long"].split("Подробнее:")[-1].strip()
        await msg.answer(f"{escape_markdown(ai_explanation)}\n\nПодробнее: {escape_markdown(doc)}", reply_markup=details_kb, parse_mode='MarkdownV2')
    except Exception as e:
        await msg.answer(f"Ошибка при обращении к AI: {e}", reply_markup=details_kb)

@router.message(lambda m: m.text == "⬅️ К темам")
async def back_to_topics(msg: Message):
    await msg.answer("Выберите тему:", reply_markup=topics_kb)

@router.message(lambda m: m.text == "⬅️ В меню")
async def back_to_menu(msg: Message):
    await msg.answer("Главное меню:", reply_markup=main_menu_kb)
