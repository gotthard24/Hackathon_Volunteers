import re
import organisations

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
    def __init__(self):
        self.options = ['m', 'o', 's', 'a', 'w', 'q']    
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
        Old/Disabled/Sick Support (O)
              Social/Poor Support (S)
                   Animal Support (A)
                    Women Support (W)
                             BACK (Q)
        """
        print(output)
        
    def option_choice(self, *funcs):
        while True:
            self.show_options()
            userinput = input("> ").lower()
            if userinput in self.options:
                if userinput == 'm':
                    funcs[0]
                elif userinput == 'o':
                    funcs[1]
                elif userinput == 's':
                    funcs[2]
                elif userinput == 'a':
                    funcs[3]
                elif userinput == 'w':
                    funcs[4]
                elif userinput == 'q':
                    break
            else:
                print("\nThere is no such option\nPlease try again")
       
    def city_input(self):
        userinput = is_valid_str(input("Enter your city")).lower()
        return userinput
        
    def main(self):
        while True:
            Main.show_user_menu()
            userinput = input("> ").lower()
            if userinput in self.volunteer_or_donate:
                if userinput == 'v':
                    user_city = self.city_input()
                    self.option_choice()
                elif userinput == 'd':
                    self.option_choice()
                elif userinput == 'q':
                    break
            else:
                print("\nThere is no such option\nPlease try again")
                
support = Main()
support.main()