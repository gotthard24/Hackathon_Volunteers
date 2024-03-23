from tkinter import *
from tkinter import ttk 
import os
import Lonlendelon


dir_path = os.path.dirname(os.path.realpath(__file__))
 
root = Tk()     # создаем корневой объект - окно
root.title("Volounterr finder 0.1")     # устанавливаем заголовок окна

def finish():
    root.destroy()  # ручное закрытие окна и всего приложения
    print("Закрытие приложения")

root.geometry("600x400+300+150")    # устанавливаем размеры окна
icon = PhotoImage(file = dir_path+r'/resources/volunteer_5944552.png')
root.iconphoto(True, icon)

label = Label(text="Welcome to Volounteer finder") # создаем текстовую метку
label.pack()    # размещаем метку в окне

def take_user_input():
    btn1.destroy()
    label1.destroy()
    user_input=entry1.get()
    entry1.destroy()
    result=Lonlendelon.make_result_list(user_input)
    label2.config(text=f'{result[0]}')
    label3.config(text=f'{result[1]}')
    label4.config(text=f'{result[2]}')
    label2.pack()
    label3.pack()
    label4.pack()



label1=ttk.Label(text='What is your city?')
label2=ttk.Label()
label3=ttk.Label()
label4=ttk.Label()
entry1= ttk.Entry()
btn1= ttk.Button(text='Confirm',command=take_user_input)
progressbar=ttk.Progressbar(orient="horizontal", length=150)
progressbar.pack()
label1.pack()
entry1.pack()
btn1.pack()



root.protocol("WM_DELETE_WINDOW", finish)

root.mainloop()