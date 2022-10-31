from tkinter import *

def change():
    button1['bg'] = '#000000'
    button1['activebackground'] = "#555555"
    button1['fg'] = '#ffffff'
    button1['activeforeground'] = '#ffffff'

root = Tk()

button1 = Button(text="Change", width=15, height=10)

button1.config(command=change)

button1.pack()

root.mainloop()



