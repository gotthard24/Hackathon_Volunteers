import organisations as o
import lonlendelon

def city_input(userinput):
        userwords = userinput.split()
        new_userwords = []
        for word in userwords:
            if word[0] == '‘' and len(word) > 1:
                new_word = word[0] + word[1].upper() + word[2:]
                new_userwords.append(new_word)
            else:
                new_userwords.append(word.capitalize())
        userinput = ' '.join((word for word in new_userwords))
        return userinput

            
def final_city_list_generation(userinput):
    cities_by_distance = lonlendelon.make_result_list(userinput)
    final_cities = []
    distance = 0
    counter = 0
    while distance < 0.2:                   
        final_cities.append(cities_by_distance[counter][0])
        distance = cities_by_distance[counter][1]
        counter += 1      
        
    return final_cities    


def print_donate_result(bot, chat_id, result_list):
    message = "<b>Available organizations to donate in Israel:</b>\n\n"
    for item in result_list:
        message += " ".join(item) + "\n"
    bot.send_message(chat_id, message, parse_mode="HTML")

def print_volunteer_result(bot, chat_id, list_of_lists):
    message = "<b>Available organizations to volunteer in closest to you cities:</b>\n\n"
    tuple_list = list_of_lists[0]
    for tuple in tuple_list:
        message += f"<b>Organisation:</b> {tuple[0]}\n"
        message += f"<b>Location:</b> {tuple[1]}\n"
        message += f"<b>Link for volunteers:</b> {tuple[2]}\n"
        message += f"<b>Description:</b> {tuple[3]}\n\n"
    bot.send_message(chat_id, message, parse_mode="HTML")
    
# def print_volunteer_result(bot, chat_id, list_of_lists):
#     message = "<b>Available organizations to volunteer in closest to you cities:</b>\n\n"
#     for tuple_list in list_of_lists:
#         if tuple_list is not None:
#             for tuple in tuple_list:
#                 message += f"<b>Organisation:</b> {tuple[0]}\n"
#                 message += f"<b>Location:</b> {tuple[1]}\n"
#                 message += f"<b>Link for volunteers:</b> {tuple[2]}\n"
#                 message += f"<b>Description:</b> {tuple[3]}\n\n"
#     bot.send_message(chat_id, message, parse_mode="HTML")
 