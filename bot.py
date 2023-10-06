import telebot
TOKEN = '6409960994:AAGJBzFwKHxEnQghxTX7GWJnOY94BCSXxow'

from telebot import types

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start']) 
def welcome(message):
	sti = open('welcome.webp', 'rb')
	bot.send_sticker(message.chat.id, sti)

	markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
	item1 = types.KeyboardButton("Мой репозиторий🤡")
	item2 = types.KeyboardButton("Написать мне в личку🤢")

	markup.add(item1, item2)

	bot.send_message(message.chat.id, "Привет тебе от краба, {0.first_name}!".format(message.from_user, bot.get_me()),
		parse_mode='html', reply_markup=markup)
@bot.message_handler(content_types=['text'])
def lalala(message):
	if message.chat.type == 'private':
		if message.text == 'Мой репозиторий🤡':
			bot.send_message(message.chat.id, 'https://github.com/AndreyRyadnovQA')
		elif message.text == 'Написать мне в личку🤢':
			bot.send_message(message.chat.id, 'https://t.me/And_reyyyyy')
		else:
			bot.send_message(message.chat.id, 'Я пока глуп для такого😢')

bot.polling(none_stop=True)







#Автор t.me/WokireS

