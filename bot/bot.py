import logging
import weather
import time
#import keyboards as kb
from aiogram import Bot, Dispatcher, executor, types
from daemon import runner

API_TOKEN = '1041174401:AAGlAIJPWwRe_jD5j97Hm8dUI25o9SdIuro' 

logging.basicConfig(level=logging.DEBUG)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

class App():

    def __init__(self):
        self.stdin_path = '/dev/null'
        self.stdout_path = '/dev/tty'
        self.stderr_path = '/dev/tty'
        self.pidfile_path =  '/var/run/testdaemon/testdaemon.pid'
        self.pidfile_timeout = 5
           
    def run(self):
        while True:
            #Main code goes here ...
            @dp.message_handler(commands=['start'])
            async def send_welcome(message: types.Message):
            	markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True, row_width=3)
            	btn_weather = types.KeyboardButton('Погода')
            	btn_help = types.KeyboardButton('help')
            	btn_youtube = types.KeyboardButton('youtube')
            	btn_twitch = types.KeyboardButton('twitch')
            	markup.add(btn_weather, btn_help, btn_youtube, btn_twitch)
            	greeting = f"<b>Hello, {message.from_user.first_name} {message.from_user.last_name}</b>!\nChoose what do you want: "
            	await bot.send_message(message.chat.id, greeting, parse_mode='html', reply_markup=markup)

            @dp.message_handler(content_types=['text'])
            async def mess(message):

            	get_message_bot = message.text.strip().lower()

            	if get_message_bot == 'погода':
            		await message.reply('Температура сейчас ' + str(weather.get_weather()[0]) + '°C' + '\n' + 
    					'Ощущается как ' + str(weather.get_weather()[1]) + '°C' + '\n' + str.title(weather.get_weather()[2]) +
    					'\n' + 'Скорость ветра ' + str(weather.get_weather()[3]) + 'м/с' + '\n' + 
    					'Давление ' + str(weather.get_weather()[4]) + 'мм')
            	elif get_message_bot == 'youtube':
            		markup = types.InlineKeyboardMarkup()
            		markup.add(types.InlineKeyboardButton("Youtube", url="https://www.youtube.com/"))
            		final_message = "Youtube <a href='https://www.youtube.com/'>Главная</a>"
            		await bot.send_message(message.chat.id, final_message, parse_mode='html', reply_markup=markup)
            	elif get_message_bot == 'twitch':
            		markup = types.InlineKeyboardMarkup()
            		markup.add(types.InlineKeyboardButton("Посмотреть стрим", url="https://www.twitch.tv/t0xii"))
            		final_message = "<a href='https://www.twitch.tv/t0xii'></a>"
            		await bot.send_message(message.chat.id, final_message, parse_mode='html', reply_markup=markup)
            	#elif get_message_bot == 'help':
            	#markup = types.InlineKeyboardMarkup()
            	#markup.add(types.InlineKeyboardButton("Информация о боте", url="Мой будущий сайт"))
            if __name__ == '__main__':
            	executor.start_polling(dp, skip_updates=True)
            #Note that logger level needs to be set to logging.DEBUG before this shows up in the logs
            logger.debug("Debug message")
            logger.info("Info message")
            logger.warn("Warning message")
            logger.error("Error message")
            time.sleep(10)

app = App()
logger = logging.getLogger("DaemonLog")
logger.setLevel(logging.INFO)
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
handler = logging.FileHandler("/var/log/testdaemon/testdaemon.log")
handler.setFormatter(formatter)
logger.addHandler(handler)

daemon_runner = runner.DaemonRunner(app)
#This ensures that the logger file handle does not get closed during daemonization
daemon_runner.daemon_context.files_preserve=[handler.stream]
daemon_runner.do_action()
