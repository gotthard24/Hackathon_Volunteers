import telebot
from telebot import types
from telebot.types import ReplyKeyboardRemove

TOKEN = "7044408816:AAE-A9JwCxXjZkjuFRAXfE9cmx9AomdloP0"

bot = telebot.TeleBot(TOKEN)

user_states = {}
user_states_btns = {}

keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
empty_keyboard = types.ReplyKeyboardRemove()
volunteer_btn = types.KeyboardButton("Volunteer")
donate_btn = types.KeyboardButton("Donate")
keyboard.add(volunteer_btn, donate_btn)

@bot.message_handler(commands=['start'])
def start(message):
    output = """
    Hi there, i am an Israel Volunteer Helper bot
    I can help you to find volunteer organisations
    closest to you.
    Choose any option to continue
    """
    bot.send_message(message.chat.id, output, reply_markup=keyboard)

@bot.message_handler(func=lambda message: message.text == "Volunteer")
def volunteer_handler(message):
    user_states_btns[message.chat.id] = 'Volunteer'
    bot.send_message(message.chat.id, "Please enter your city:")
    user_states[message.chat.id] = 'wait_for_input'

@bot.message_handler(func=lambda message: message.text == "Donate")
def donate_handler(message):
    user_states_btns[message.chat.id] = 'Donate'
    bot.send_message(message.chat.id, "Choose interesting donation option for you:", reply_markup=topic_buttons())

@bot.message_handler(func=lambda message: user_states.get(message.chat.id) == 'wait_for_input')
def handle_user_input(message):
    bot.send_message(message.chat.id, f"You entered: {message.text}")
    bot.send_message(message.chat.id, "Choose interesting volunteer option for you:", reply_markup=topic_buttons())
    del user_states[message.chat.id]
    
def topic_buttons():
    keyboard = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    military_btn = types.KeyboardButton("Military")
    health_btn = types.KeyboardButton("Health")
    social_btn = types.KeyboardButton("Social")
    animals_btn = types.KeyboardButton("Animals")
    keyboard.add(military_btn, health_btn, social_btn, animals_btn)
    return keyboard

@bot.message_handler(func=lambda message: message.text == "Military")
def military_handler(message):
    user_state_btns = user_states_btns.get(message.chat.id)
    if user_state_btns == 'Volunteer':
        bot.send_message(message.chat.id, "Before was Volunteer")
    elif user_state_btns == 'Donate':
        bot.send_message(message.chat.id, "Before was pressed Donate")
    

if __name__ == '__main__':
    bot.infinity_polling()