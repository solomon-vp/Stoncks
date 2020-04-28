import yfinance as yf
import telebot
import parser

bot = telebot.TeleBot('1200593659:AAFMpll7K1qnrQWCF5mKHVEJK8QGJKtQjc8')

keyboard1 = telebot.types.ReplyKeyboardMarkup(True, True)
keyboard1.row('Акции', 'Валюты', 'Криптовалюты')

keyboard2 = telebot.types.ReplyKeyboardMarkup(True, True)
keyboard2.row('Apple', 'Amazon', 'Tesla')

keyboard3 = telebot.types.ReplyKeyboardMarkup(True, True)
keyboard3.row('USD', 'EURO', 'JPY')

keyboard4 = telebot.types.ReplyKeyboardMarkup(True, True)
keyboard4.row('Bitcoin', 'ETH', 'NEO')


# @bot.message_handler(content_types=['text'])
@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Выберите интересующие Вас активы", reply_markup=keyboard1)
    # bot.register_next_step_handler(message, get_inf)


@bot.message_handler(content_types=['text'])
def get_inf(message):
    if message.text == "Акции":
        bot.register_next_step_handler(message, get_stocks)
        bot.send_message(message.from_user.id, "Выберите интересующие Вас акции", reply_markup=keyboard2)
    elif message.text == 'Валюты':
        bot.register_next_step_handler(message, get_currency)
        bot.send_message(message.from_user.id, "Выберите интересующую Вас валюту", reply_markup=keyboard3)
    elif message.text == 'Криптовалюты':
        bot.register_next_step_handler(message, get_crypto)
        bot.send_message(message.from_user.id, "Выберите интересующую Вас криптовалюту", reply_markup=keyboard4)
    else:
        bot.send_message(message.from_user.id, "Выберите актив из списка", reply_markup=keyboard1)


@bot.message_handler(content_types=['text'])
def get_stocks(message):
    if message.text == "Apple":
        stocks = yf.Ticker('AAPL')
        bot.send_message(message.from_user.id, 'Apple stock prise is '+str(stocks.info['previousClose'])+str(' USD'))
    elif message.text == "Amazon":
        stocks = yf.Ticker('AMZN')
        bot.send_message(message.from_user.id, str('Amazon stock prise is '+stocks.info['previousClose'])+str(' USD'))
    if message.text == "Tesla":
        stocks = yf.Ticker('TSLA')
        bot.send_message(message.from_user.id, 'Tesla stock prise is '+str(stocks.info['previousClose'])+str(' USD'))


def get_currency(message):
    if message.text == "USD":
        bot.send_message(message.from_user.id, parser.usd())
    if message.text == "EURO":
        bot.send_message(message.from_user.id, parser.euro())
    if message.text == "JPY":
        bot.send_message(message.from_user.id, parser.jpy())

def get_crypto(message):
    bot.send_message(message.from_user.id, "Выберите интересующую Вас криптовалюту", reply_markup=keyboard4)


bot.polling(none_stop=True, interval=0)