from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

# Создаем кнопки
button1 = KeyboardButton('Кнопка 1')
button2 = KeyboardButton('Кнопка 2')
button3 = KeyboardButton('Кнопка 3')

# Создаем клавиатуру и добавляем кнопки
main_menu_keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
main_menu_keyboard.add(button1, button2, button3)