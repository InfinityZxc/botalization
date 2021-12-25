import telebot
from telebot import types
from telebot import custom_filters
import os

tutorial_page = 0 
hi_count = 0 
bug_story_count = 0

TOKEN = os.environ["TOKEN"]
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
	bot.reply_to(message, "Привет, цель этого небольшого бота - продвижение чуть менее небольшой игры. Вы всегда можете получить ссылку на игру с помощью команды game")

@bot.message_handler(commands=['game'])
def send_game(message):
	bot.send_message(message.chat.id, "https://infinityzxc.itch.io/catalization")
	bot.send_message(message.chat.id, "играйте и веселитесь\*_*/")

@bot.message_handler(text=['hi','hello'])
def filter_hi(message):
	global hi_count
	hi_count = hi_count + 1
	if hi_count == 1:
		bot.reply_to(message, "Привет, {name}!".format(name=message.from_user.first_name))
	elif hi_count == 2:
		bot.reply_to(message, "Привет снова, {name}!".format(name=message.from_user.first_name))
	elif hi_count == 3:
		bot.reply_to(message, "Привет третий раз, {name}.".format(name=message.from_user.first_name))
	elif hi_count == 4:
		bot.reply_to(message, "{name}, хватит уже!".format(name=message.from_user.first_name))
	elif hi_count == 5:
		bot.reply_to(message, "Мы уже поздаровались :/")
	elif hi_count == 6:
		bot.reply_to(message, "6, шесть приветсвий, вам не много?")
	elif hi_count == 7:
		bot.reply_to(message, "Пока, {name}.".format(name=message.from_user.first_name))
	else:
		ans =  "Привет, {name}, поздаровавшийся {count} раз.".format(name=message.from_user.first_name, count = hi_count)
		bot.reply_to(message, ans)



@bot.message_handler(commands=['tutorial'])
def send_tutorial_1(message):
	global tutorial_page
	if tutorial_page == 0:
		img1 = open('tutorial_1.jpg', 'rb')
		bot.send_photo(message.chat.id, img1)
		bot.send_message(message.chat.id, "Чтобы сделать ход, перетащите одну из двух плиток справа внизу в какое-нибудь незанятое место рядом с уже существующей плиткой. Существует 3 типа, каждый из которых по-разному взаимодействует с глюком: \n\n Деревья более продуктивны. \n Вода невосприимчива к сбоям. \n Горы должны быть атакованы дважды, прежде чем возникнут сбои.")
		tutorial_page = 1
	else:
		bot.send_message(message.chat.id, "Туториал уже запущен, используйте /next чтобы посмотреть следующую страницу.")

@bot.message_handler(commands=['next'])
def send_tutorial_2(message):
	global tutorial_page
	if tutorial_page == 1:
		img2 = open('tutorial_2.jpg', 'rb')
		bot.send_photo(message.chat.id, img2)
		bot.send_message(message.chat.id, "С некоторого момента времени глюк начнет захватывать плитки, больше за ход с течением времени. \n\n Как противостоять его расширению?\n\n Это довольно просто: без сбоев плитки производят монеты (разное количество для каждого типа), каждый ход доступны две способности для монет. Нажмите один раз на молнию и плитку без сбоев, чтобы очистить ее. Нажмите на снежинку, чтобы остановить распространение глюков до следующего поворота. \n\n Укладка небольших групп плиток одного типа вместе дает больше монет.")
		tutorial_page = 0
	else:
		bot.send_message(message.chat.id, "Туториал ещё не запущен, используйте /tutorial чтобы начать.")
		
@bot.message_handler(commands=['story'])
def tell_story(message):
	global bug_story_count
	stories = ["Из-за того, что кто-то в спешке добавлял сетку, она создаётся каждый раз при перезапуске игры и не удаляется, так можно сломать игру за примерно десяток попыток", "В одной строке вместо - оказался + и теперь игра намного сложнее, чем задумывалась(но всё еще проходима)", "Я лично без понятия кто делает арты и это меня пугает.", "Начальные клетки должны случайно меняться из раза в раз, но они так не делают, хмм//"]
	ans = ""
	if bug_story_count < 4:
		ans = stories[bug_story_count]
		bug_story_count = bug_story_count + 1
		bot.send_message(message.chat.id, ans)
	else:
		bot.send_message(message.chat.id, "Истории закончились, теперь они пойдут с начала :(")
		bug_story_count = 0



@bot.message_handler(func=lambda message: True)
def smile_for_all(message):
	bot.send_message(message.chat.id, "\*_*√")

bot.add_custom_filter(custom_filters.TextMatchFilter())

bot.infinity_polling()