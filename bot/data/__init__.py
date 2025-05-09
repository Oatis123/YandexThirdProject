# Примерные уроки Python (можно добавить больше по аналогии)
LESSONS = [
    ("1_Переменные.txt", "Переменные — это имена для хранения данных.\n\nПример:\nx = 5\ny = 'строка'\nprint(x, y)"),
    ("2_Условия.txt", "Условия позволяют выполнять код в зависимости от логики.\n\nПример:\nx = 10\nif x > 5:\n    print('x больше 5')\nelse:\n    print('x меньше или равен 5')"),
    ("3_Циклы.txt", "Циклы позволяют повторять действия.\n\nПример for:\nfor i in range(3):\n    print(i)\n\nПример while:\ni = 0\nwhile i < 3:\n    print(i)\n    i += 1"),
    ("4_Функции.txt", "Функции позволяют переиспользовать код.\n\nПример:\ndef add(a, b):\n    return a + b\nprint(add(2, 3))"),
    ("5_Классы.txt", "Классы — основа ООП.\n\nПример:\nclass Person:\n    def __init__(self, name):\n        self.name = name\np = Person('Вася')\nprint(p.name)"),
    ("6_Модули.txt", "Модули позволяют структурировать код.\n\nПример:\nimport math\nprint(math.sqrt(16))"),
    ("7_Работа_с_файлами.txt", "Работа с файлами в Python.\n\nПример:\nwith open('file.txt', 'w') as f:\n    f.write('Hello!')"),
    ("8_Исключения.txt", "Обработка ошибок через try/except.\n\nПример:\ntry:\n    1/0\nexcept ZeroDivisionError:\n    print('Деление на ноль!')"),
    ("9_Списки_и_словари.txt", "Списки и словари — основные коллекции.\n\nПример списка:\nlst = [1,2,3]\nprint(lst[0])\n\nПример словаря:\nd = {'a': 1}\nprint(d['a'])"),
    ("10_ООП.txt", "ООП — объектно-ориентированное программирование.\n\nПример:\nclass Animal:\n    def speak(self):\n        print('Звук')\nclass Dog(Animal):\n    def speak(self):\n        print('Гав!')\nd = Dog()\nd.speak()")
]

def create_python_lessons():
    import os
    course_path = os.path.join(os.path.dirname(__file__), 'python_course')
    os.makedirs(course_path, exist_ok=True)
    for filename, content in LESSONS:
        with open(os.path.join(course_path, filename), 'w', encoding='utf-8') as f:
            f.write(content)

if __name__ == "__main__":
    create_python_lessons()