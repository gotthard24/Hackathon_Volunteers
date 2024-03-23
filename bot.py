import telebot
from telebot import types
from telebot.types import ReplyKeyboardRemove
import bot_functions
import organisations as o

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

@bot.message_handler(func=lambda message: user_states.get(message.chat.id) == 'wait_for_input' or user_states.get(message.chat.id) == 'multiple_choice')
def handle_user_input(message):
    user_city = bot_functions.city_input(message.text)  
    if user_states.get(message.chat.id) == 'multiple_choice':
        city = o.precise_select_city(user_city)
    else:
        city = o.select_city(user_city)
    if city == None:
        bot.send_message(message.chat.id, f"Oops, city {user_city} not found\n Maybe you meant any of this?\n")
        user_states[message.chat.id] = "wait_for_input" 
        query_parts = [user_city[i:i+3] for i in range(0, len(user_city), 3)]
        for part in query_parts:
            city = o.select_city(part)
            if city != None:
                bot.send_message(message.chat.id, city) 
    elif len(city) > 1:
        bot.send_message(message.chat.id, f"There are more then one\n You meant any of this? \n{city}") 
        user_states[message.chat.id] = "multiple_choice" 
    else:     
        del user_states[message.chat.id]
        bot.send_message(message.chat.id,"One minute, Your request is being processed ")
        user_states[message.chat.id] = "cc"  
        global cities
        cities = bot_functions.final_city_list_generation(user_city)
        handler_correct_input(message)   
  
@bot.message_handler(func=lambda message: user_states.get(message.chat.id) == 'cc')
def handler_correct_input(message):
    del user_states[message.chat.id]
    user_states_btns[message.chat.id] = "Volunteer"
    bot.send_message(message.chat.id, "Request completed")
    bot.send_message(message.chat.id, "Choose interesting volunteer option for you:", reply_markup=topic_buttons())
    
@bot.message_handler(func=lambda message: message.text == "Donate")
def donate_handler(message):
    user_states_btns[message.chat.id] = 'Donate'
    bot.send_message(message.chat.id, "Choose interesting donation option for you:", reply_markup=topic_buttons())
    
def topic_buttons():
    keyboard = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    military_btn = types.KeyboardButton("Military")
    health_btn = types.KeyboardButton("Health")
    social_btn = types.KeyboardButton("Social")
    animals_btn = types.KeyboardButton("Animals")
    keyboard.add(military_btn, health_btn, social_btn, animals_btn)
    return keyboard

def result_by_btn_state_check(message):
    user_state_btns = user_states_btns.get(message.chat.id)
    if user_state_btns == 'Volunteer':
        bot_functions.print_volunteer_result(bot, message.chat.id, o.select_volunteers(cities, message.text))
    elif user_state_btns == 'Donate':
        bot_functions.print_donate_result(bot, message.chat.id, o.select_donate(message.text))

@bot.message_handler(func=lambda message: message.text == "Military")
def military_handler(message):
    result_by_btn_state_check(message)
        
@bot.message_handler(func=lambda message: message.text == "Health")
def health_handler(message):
    result_by_btn_state_check(message)
        
@bot.message_handler(func=lambda message: message.text == "Social")
def social_handler(message):
    result_by_btn_state_check(message)
        
@bot.message_handler(func=lambda message: message.text == "Animals")
def animals_handler(message):
    result_by_btn_state_check(message)

if __name__ == '__main__':
    bot.infinity_polling()