import re
import lonlendelon 
import organisations as o

def is_int(var):
    while True:
        try:
            integer_value = int(var)
            return integer_value
        except ValueError:
            print("It's not a number. Please try again")
            var = input("Enter the number:\n>  ")
                        
def is_valid_str(var):
    while True:
        try:
            if re.match(r'[A-Za-z]', var):               
                return var.capitalize()
        except ValueError:
            print("It's not a valid string. Please try again")
            var = input("Enter the string:\n>  ")
        
            
class Main():
    MILITARY = 'Military'
    HEALTH = 'Health'
    SOCIAL = 'Social'
    ANIMAL = 'Animals'
           
    def __init__(self):
        self.options = ['m', 'o', 's', 'a', 'q']    
        self.volunteer_or_donate = ['v', 'd', 'q']
                   
    @staticmethod     
    def show_user_menu():
        print("\nChoose option please")
        output = """
           Volunteer (V)
              Donate (D)
                QUIT (Q)
        """
        print(output)
        
    @staticmethod    
    def show_options():
        print("\nChoose option please")
        output = """
          Military Forces Support (M)
      Old/Disabled/Health Support (O)
              Social/Poor Support (S)
                   Animal Support (A)
                             BACK (Q)
        """
        print(output)
        
    def print_donate_result(self, list):
        print("\nAvailable organistions to danate\n")
        for item in list:
            for i in range(len(item)):
                print(item[i], end= "   ")
            print('\n')
            
    def print_volunteer_result(self, list):
        print("\nAvailable organistions to volunteer in your city\n")
        for item in list:
            for i in range(len(item)):
                print(item[i], end= "   ")
            print('\n')
        
    def option_choice(self, vol_or_donate, *funcs):
        options_mapping = {
            'm': funcs[0],
            'o': funcs[1],
            's': funcs[2],
            'a': funcs[3]
        }

        while True:
            self.show_options()
            userinput = input("> ").lower()
            
            if userinput in options_mapping:
                result = options_mapping[userinput]
                if vol_or_donate == 'donate':
                    self.print_donate_result(result)
                else:
                    pass
                break
            elif userinput == 'q':
                break
            else:
                print("\nThere is no such option\nPlease try again")

       
    def city_input(self):
        userinput = is_valid_str(input("Enter your city\n> "))
        userinput = ' '.join((word.capitalize() for word in userinput.split()))
        return userinput
    
    def input_filter(self):
        while True:
            user_city = self.city_input()
            city = o.select_city(user_city)
            if user_city == 'Exit':
                break
            elif city == None:      
                print(f"Oops, city {user_city} not found\n Maybe you meant any of this\n")              
                query_parts = [user_city[i:i+3] for i in range(0, len(user_city), 3)]
                for part in query_parts:
                    city = o.select_city(part)
                    if city != None:
                       print(city) 
            elif len(city) > 1:
                print(f"Oops, city {user_city} not found\n Maybe you meant any of this \n{city}") 
            else:                    
                cities = lonlendelon.make_result_list(user_city)
                return cities
                    
    def main(self):
        while True:
            Main.show_user_menu()
            userinput = input("> ").lower()
            if userinput in self.volunteer_or_donate:
                if userinput == 'v':
                    cities_by_distance = self.input_filter()
                    final_cities = []
                    distance = 0
                    counter = 0
                    print("One minute, Your request is being processed ")
                    while distance < 0.2:                   
                        final_cities.append(cities_by_distance[counter][0])
                        distance = cities_by_distance[counter][1]
                        counter += 1
                    print("One minute, Your request is being processed ")
                    for city in final_cities:
                        print(city)                   
                        # self.option_choice('vol',o.select_volunteers(user_city, self.MILITARY),
                        #                         o.select_volunteers(user_city, self.HEALTH),
                        #                         o.select_volunteers(user_city, self.SOCIAL),
                        #                         o.select_volunteers(user_city, self.ANIMAL))
                elif userinput == 'd':
                    self.option_choice('donate',o.select_donate(self.MILITARY),
                                                o.select_donate(self.HEALTH),
                                                o.select_donate(self.SOCIAL),
                                                o.select_donate(self.ANIMAL))
                elif userinput == 'q':
                    break
            else:
                print("\nThere is no such option\nPlease try again")
                
support = Main()
support.main()
# print(support.city_input())

# print(lonlendelon.make_result_list('Tel Aviv'))
# organisations.test()