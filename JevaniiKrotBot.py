import telebot
from utilities import ConversionException, CurrencyConverter
from config import currencies, TOKEN

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=["start", "help"])
def handle_start_help(message: telebot.types.Message):
    text = "To start working, enter the bot command in the following format:\n<currency name> " \
           "<which currency to convert to> " \
           "<amount of currency to be converted>\n" \
           "Also, you can see a list of all of available currencies by entering the command: /values"
    bot.reply_to(message, text)


@bot.message_handler(commands=["values"])
def values(message: telebot.types.Message):
    text = "Available currency:"
    for currency in currencies.keys():
        text = "\n".join((text, currency))
    bot.reply_to(message, text)


@bot.message_handler(content_types=["text"])
def convert(message: telebot.types.Message):
    try:
        parameters = message.text.split(" ")
        if len(parameters) != 3:
            raise ConversionException("Quantity of parameters is not correct.")

        quote, base, amount = parameters
        total_base = CurrencyConverter.convert(quote, base, amount)
    except ConversionException as e:
        bot.reply_to(message, f"User error.\n{e}")
    except Exception as e:
        bot.reply_to(message, f"Command performing is failed.\n{e}")
    else:
        text = f"Price of {amount} {quote} in {base} - {float(amount)*total_base}"
        bot.send_message(message.chat.id, text)


bot.polling(none_stop=True)
