from tkinter import *
from tkinter import ttk 
import os
import main
import organisations as o

dir_path = os.path.dirname(os.path.realpath(__file__))
 
root = Tk()     # создаем корневой объект - окно
root.title("Volounterr finder 0.1")     # устанавливаем заголовок окна

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

def call_main_menu(): #main menu
    destroy_all_widgets()
    label = Label(text="Welcome to Volounteer finder")
    label.pack()
    label1 = ttk.Label(text='MENU')
    btn_menu_1 = ttk.Button(text='Volunteer')
    btn_menu_2 = ttk.Button(text='Donate',command=show_donate_options)
    btn_menu_3 = ttk.Button(text='Quit',command=finish)
    label1.pack()
    btn_menu_1.pack()
    btn_menu_2.pack()
    btn_menu_3.pack()

#Donate section

def show_donate_options(): #Donate menu
    destroy_all_widgets()
    label = Label(text="Welcome to Volounteer finder")
    label.pack()
    label2 = ttk.Label(text='In which field you want to support?')
    btn_menu_4 = ttk.Button(text='Military Forces Support',command=donate_military)
    btn_menu_5 = ttk.Button(text='Old/Disabled/Health Support',command=donate_health)
    btn_menu_6 = ttk.Button(text='Social/Poor Support',command=donate_Social)
    btn_menu_7 = ttk.Button(text='Animal Support',command=donate_animals)
    btn_menu_8 = ttk.Button(text='Back',command=call_main_menu)
    label2.pack()
    btn_menu_4.pack()
    btn_menu_5.pack()
    btn_menu_6.pack()
    btn_menu_7.pack()
    btn_menu_8.pack()

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
    label = Label(text="Welcome to Volounteer finder")
    label.pack()
    label2= Label(text='Available organistions to donate')
    label2.pack()
    text_result=Text(wrap='word')
    text_result.insert(1.0,f"{print_donate_result(title)}")
    text_result.pack()
    text_result.bind("<Key>", disable_text_widget)
    btn_menu_8 = ttk.Button(text='Back',command=call_main_menu)
    btn_menu_8.pack()

#Volonteer section
    








# Start 
call_main_menu()

# def take_user_input():
#     btn1.destroy()
#     label1.destroy()
#     user_input=entry1.get()
#     entry1.destroy()
#     result=lonlendelon.make_result_list(user_input)
#     label2.config(text=f'{result[0]}')
#     label3.config(text=f'{result[1]}')
#     label4.config(text=f'{result[2]}')
#     label2.pack()
#     label3.pack()
#     label4.pack()

root.protocol("WM_DELETE_WINDOW", finish)

root.mainloop()

# print(print_donate_result())