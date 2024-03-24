from tkinter import *
from tkinter import ttk 
from tkinter.scrolledtext import ScrolledText
import os
import organisations as o
import re
import lonlendelon


dir_path = os.path.dirname(os.path.realpath(__file__))
 
root = Tk()     # создаем корневой объект - окно
root.title("Volounterr finder 0.1")     # устанавливаем заголовок окна

def finishesc(event):
    root.destroy()  # ручное закрытие окна и всего приложения
    print("Закрытие приложения")

def finish():
    root.destroy()  # ручное закрытие окна и всего приложения
    print("Закрытие приложения")   

root.geometry("800x600+150+75")    # устанавливаем размеры окна
icon = PhotoImage(file = dir_path+r'/resources/volunteer_5944552.png')
root.iconphoto(True, icon)

label = Label(text="Welcome to Volounteer finder") # создаем текстовую метку
label.pack()    # размещаем метку в окне

def destroy_all_widgets(): #destroy all widgets
    for widget in root.winfo_children():
        widget.destroy()

root.bind("<KeyPress-Escape>", finishesc)

def call_main_menu(): #main menu
    destroy_all_widgets()
    label = Label(text="Welcome to Volounteer finder",foreground="#01579B",font="Verdana 16 bold roman")
    label.pack(pady=10)
    label1 = ttk.Label(text='MENU',font="Verdana 14 bold roman")
    btn_menu_1 = ttk.Button(text='Volunteer',command=city_select,style="big.TButton")
    btn_menu_2 = ttk.Button(text='Donate',command=show_donate_options,style="big.TButton")
    btn_menu_3 = ttk.Button(text='Quit',command=finish,style="big.TButton")
    label1.place(relx=.5, rely=.2,anchor='n')
    btn_menu_1.place(relx=.3, rely=.4,anchor='c',relheight=.09,relwidth=.15)
    btn_menu_2.place(relx=.7, rely=.4,anchor='c',relheight=.09,relwidth=.15)
    btn_menu_3.place(relx=.5, rely=.6, anchor='c',relheight=.09,relwidth=.15)
    

#Donate section

def show_donate_options(): #Donate menu
    destroy_all_widgets()
    label = Label(text="Welcome to Volounteer finder",foreground="#01579B",font="Verdana 16 bold roman")
    label.pack(pady=10)
    label2 = ttk.Label(text='In which field you want to support?',font="Verdana 14 bold roman")
    btn_menu_4 = ttk.Button(text='Military Forces Support',command=donate_military,style="small.TButton")
    btn_menu_5 = ttk.Button(text='Old/Disabled/Health Support',command=donate_health,style="small.TButton")
    btn_menu_6 = ttk.Button(text='Social/Poor Support',command=donate_Social,style="small.TButton")
    btn_menu_7 = ttk.Button(text='Animal Support',command=donate_animals,style="small.TButton")
    btn_menu_8 = ttk.Button(text='Back',command=call_main_menu,style="small.TButton")
    label2.place(relx=.5, rely=.2,anchor='n')
    btn_menu_4.place(relx=.35, rely=.4,anchor='c',relheight=.07,relwidth=.25)
    btn_menu_5.place(relx=.65, rely=.4,anchor='c',relheight=.07,relwidth=.25)
    btn_menu_6.place(relx=.35, rely=.5,anchor='c',relheight=.07,relwidth=.25)
    btn_menu_7.place(relx=.65, rely=.5,anchor='c',relheight=.07,relwidth=.25)
    btn_menu_8.place(relx=.5, rely=.8, anchor='c',relheight=.07,relwidth=.25)

#Donate funcs

def donate_animals():
    title='Animals'
    show_donate_result(title)

def donate_military():
    title='Military'
    show_donate_result(title)

def donate_health():
    title='Health'
    show_donate_result(title)

def donate_Social():
    title='Social'
    show_donate_result(title)

def print_donate_result(title):
    result = o.select_donate(title)
    mylist=[]
    for x,y in result:
        mylist.append(x)
        y='URL: '+y+'\n'
        mylist.append(y)
        result='\n'.join(mylist)
    return result 

def disable_text_widget(event): #Disable ability to print in Text()
    return "break"

def show_donate_result(title):
    destroy_all_widgets()
    label = Label(text="Welcome to Volounteer finder",foreground="#01579B",font="Verdana 16 bold roman")
    label.pack(pady=10)
    label2= Label(text='Available organistions to donate',font="Verdana 14 bold roman")
    label2.pack()
    text_result=Text(wrap='word',font="Verdana 10 normal roman")
    text_result.insert(1.0,f"{print_donate_result(title)}")
    text_result.place(relx=.5, rely=.5, anchor='c',relheight=.7,relwidth=.9)
    text_result.bind("<Key>", disable_text_widget)
    btn_menu_8 = ttk.Button(text='Back',command=call_main_menu,style="small.TButton")
    btn_menu_8.place(relx=.5, rely=.9, anchor='c',relheight=.07,relwidth=.25)

#Volonteer section

def delete_char(entry): #fix backspace fisrtletter issue
    entry.config(validate="none")
    entry.delete(len(entry.get()) - 1)
    entry.config(validate="key")

errmsg = StringVar() 

def is_valid(newval): 
    result = re.match("^[A-Za-z'‘ ]+$", newval) is not None   
    if not result:
        errmsg.set("Please use only english letters and ' for apostrophe!")
    else:
        errmsg.set("")
    return result

check = (root.register(is_valid), "%P")

def city_select(): #get user input
    destroy_all_widgets()
    label = Label(text="Welcome to Volounteer finder",foreground="#01579B",font="Verdana 16 bold roman")
    label.pack(pady=10)
    label2 = ttk.Label(text='Please input your city',font="Verdana 14 bold roman")
    label2.pack()
    entry = ttk.Entry(validate="key", validatecommand=check, font="Verdana 10 normal roman")
    entry.bind("<BackSpace>", lambda event: delete_char(entry))
    entry.place(relx=.5, rely=.2, anchor='c',relheight=.05,relwidth=.25)
    error_label = ttk.Label(foreground="red", textvariable=errmsg, wraplength=500,font="Verdana 10 normal roman")
    error_label.place(relx=.5, rely=.3, anchor='c',relheight=.1,relwidth=.5)
    btn_menu_9 = ttk.Button(text='Enter',command=lambda :find_city(entry.get()),style="small.TButton")
    btn_menu_9.place(relx=.5, rely=.4, anchor='c',relheight=.05,relwidth=.2)
    label2 = ttk.Label(text='Please be patient...',font="Verdana 14 bold roman")
    label2.place(relx=.5, rely=.5, anchor='c',relheight=.05,relwidth=.3)
    btn_menu_8 = ttk.Button(text='Back',command=call_main_menu,style="small.TButton")
    btn_menu_8.place(relx=.5, rely=.9, anchor='c',relheight=.05,relwidth=.25)

def find_city(user_input): #work with user input
    destroy_all_widgets()
    label = Label(text="Welcome to Volounteer finder",foreground="#01579B",font="Verdana 16 bold roman")
    label.pack(pady=10)
    userwords = user_input.split()
    new_userwords = []
    for word in userwords:
        if word[0] == '‘' and len(word) > 1:
            new_word = word[0] + word[1].upper() + word[2:]
            new_userwords.append(new_word)
        else:
            new_userwords.append(word.capitalize())
    user_input = ' '.join((word for word in new_userwords))
    user_city = user_input #make it ok for tables
    city = o.precise_select_city(user_city)
    if city==None: #If not finded precise city
        city = o.select_city(user_city)
        if city !=None: 
            destroy_all_widgets()
            label = Label(text="Welcome to Volounteer finder",foreground="#01579B",font="Verdana 16 bold roman")
            label.pack(pady=20)
            label2= Label(text=f"Oops, city {user_city} not found\n Maybe you meant any of this?\n",font="Verdana 14 bold roman")
            label2.pack()
            placex=0.2
            placey=0.3
            for item in city:
                    btn = ttk.Button(text=f'{item[0]}',command=lambda: find_city(item[0]),style="small.TButton")
                    btn.place(relx=placex, rely=placey, anchor='c',relheight=.05,relwidth=.2)
                    placex+=0.2
                    if placex>0.8:
                        placey+=0.1
                        placex=0.2       
            btn_menu_1 = ttk.Button(text='Try again/change input', command=city_select,style="small.TButton")
            btn_menu_1.place(relx=.5, rely=.9, anchor='s',relheight=.05,relwidth=.25)
        else: #If not finded ILIKE city
            query_parts = [user_city[:3], user_city[-4:-1]]
            for part in query_parts:
                city = o.select_city(part)
                if city != None:
                    destroy_all_widgets()
                    label = Label(text="Welcome to Volounteer finder",foreground="#01579B",font="Verdana 16 bold roman")
                    label.pack(pady=20)
                    label2= Label(text=f"Oops, city {user_city} not found\n Maybe you meant any of this?\n",font="Verdana 14 bold roman")
                    label2.pack()
                    placex=0.2
                    placey=0.3
                    for item in city:
                            btn = ttk.Button(text=f'{item[0]}',command=lambda: find_city(item[0]),style="small.TButton")
                            btn.place(relx=placex, rely=placey, anchor='c',relheight=.05,relwidth=.2)
                            placex+=0.2
                            if placex>0.8:
                                placey+=0.1
                                placex=0.2              
                    btn_menu_1 = ttk.Button(text='Try again/change input', command=city_select)
                    btn_menu_1.place(relx=.5, rely=.9, anchor='s',relheight=.05,relwidth=.25)
                else: #If not find at all
                    destroy_all_widgets()
                    label = Label(text="Welcome to Volounteer finder",foreground="#01579B",font="Verdana 16 bold roman")
                    label.pack(pady=20)
                    label2= Label(text=f"Oops, city {user_city} not found",font="Verdana 14 bold roman")
                    label2.pack()  
                    btn_menu_1 = ttk.Button(text='Try again/change input', command=city_select)
                    btn_menu_1.place(relx=.5, rely=.9, anchor='s',relheight=.05,relwidth=.25)                     
    else: #work with finded city    
        destroy_all_widgets()
        label = Label(text="Welcome to Volounteer finder",foreground="#01579B",font="Verdana 16 bold roman")
        label.pack(pady=10)           
        cities = lonlendelon.make_result_list(user_city)
        final_cities = []
        distance = 0
        counter = 0
        while distance < 0.2:                   
            final_cities.append(cities[counter][0])
            distance = cities[counter][1]
            counter += 1
        label2 = ttk.Label(text='In which field you want to participate?',font="Verdana 14 bold roman")
        btn_menu_4 = ttk.Button(text='Military Forces Support',command= lambda :volonteer_military(final_cities),style="small.TButton")
        btn_menu_5 = ttk.Button(text='Old/Disabled/Health Support',command= lambda :volonteer_health(final_cities),style="small.TButton")
        btn_menu_6 = ttk.Button(text='Social/Poor Support',command= lambda :volonteer_Social(final_cities),style="small.TButton")
        btn_menu_7 = ttk.Button(text='Animal Support',command=lambda :volonteer_animals(final_cities),style="small.TButton")
        btn_menu_8 = ttk.Button(text='Back',command=call_main_menu,style="small.TButton")
        label2.place(relx=.5, rely=.2,anchor='n')
        btn_menu_4.place(relx=.35, rely=.4,anchor='c',relheight=.07,relwidth=.25)
        btn_menu_5.place(relx=.65, rely=.4,anchor='c',relheight=.07,relwidth=.25)
        btn_menu_6.place(relx=.35, rely=.5,anchor='c',relheight=.07,relwidth=.25)
        btn_menu_7.place(relx=.65, rely=.5,anchor='c',relheight=.07,relwidth=.25)
        btn_menu_8.place(relx=.5, rely=.8, anchor='c',relheight=.07,relwidth=.25)

# checks titles
        
def volonteer_animals(cities):
    title='Animals'
    show_volonteer_result(cities,title)

def volonteer_military(cities):
    title='Military'
    show_volonteer_result(cities,title)

def volonteer_health(cities):
    title='Health'
    show_volonteer_result(cities,title)

def volonteer_Social(cities):
    title='Social'
    show_volonteer_result(cities,title)


def print_volonteer_result(cities,title): #printing results
    result = o.select_volunteers(cities,title)
    mylist=[]
    for tuple_list in result:
            if tuple_list is not None: 
                for tuple in tuple_list:
                    mylist.append((f"Organisation: {tuple[0]}"))
                    mylist.append((f"Location: {tuple[1]}"))
                    mylist.append((f"Link for volunteers: {tuple[2]}")) 
                    mylist.append((f"Description: {tuple[3]}\n"))
                    result='\n'.join(mylist)
    return result

def disable_text_widget(event): #Disable ability to print in Text()
    return "break"

def show_volonteer_result(cities,title): #final result window
    destroy_all_widgets()
    label = Label(text="Welcome to Volounteer finder",foreground="#01579B",font="Verdana 16 bold roman")
    label.pack(pady=10)
    label2= Label(text='Clossest organisation to you:',font="Verdana 14 bold roman")
    label2.pack()
    st = ScrolledText(root ,wrap='word',font="Verdana 10 normal roman")
    st.pack(fill=BOTH, side=LEFT, expand=True)
    st.insert(1.0,f"{print_volonteer_result(cities,title)}")
    st.place(relx=.5, rely=.5, anchor='c',relheight=.7,relwidth=.9)
    st.bind("<Key>", disable_text_widget)
    btn_menu_8 = ttk.Button(text='Back',command=call_main_menu,style="small.TButton")
    btn_menu_8.place(relx=.5, rely=.9, anchor='c',relheight=.07,relwidth=.25)
# Start 
call_main_menu()

root.protocol("WM_DELETE_WINDOW", finish)

style=ttk.Style()
style.configure('small.TButton', font=(None, 10))
style.configure('big.TButton', font=(None, 14), foreground="blue")

root.mainloop()
