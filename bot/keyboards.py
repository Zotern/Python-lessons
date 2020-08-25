from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton

button_hi = KeyboardButton('Привет! 👋')
button_weather = KeyboardButton('Погода')

greet_kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(button_hi).add(button_weather)

inline_btn_hi = InlineKeyboardButton(callback_data='button1', text=str(get_weather()[0]) + '°C')
inline_kb = InlineKeyboardMarkup().add(inline_btn_hi)

markup = InlineKeyboardMarkup()
markup.add(InlineKeyboardButton("Посмотреть курсы по Unity", url="https://itproger.com/tag/unity"))