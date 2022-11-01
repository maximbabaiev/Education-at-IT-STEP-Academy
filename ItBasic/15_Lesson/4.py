from tkinter import *
from tkinter import messagebox
import pickle




HEIGHT = 550
WIDHT = 550



def reg():
    label_error = None


    frame = Frame(root, bd=10)
    frame.place(relx=0.5, rely=0.2, relwidth=0.7, relheight=0.6, anchor="n")

    label = Label(frame, text="SIGN UP", font='16')
    label.place(relwidth=1, relheight=0.1)

    label_login = Label(frame, text="Login: ")
    label_login.place(rely=0.2, relwidth=0.35, relheight=0.1)

    login_reg = Entry(frame)
    login_reg.place(relx=0.4, rely=0.2, relheight=0.1, relwidth=0.55)

    label.pas1 = Label(frame, text="Password: ")
    label.pas1.place(rely=0.4, relwidth=0.35, relheight=0.1)

    password1 = Entry(frame, show="*")
    password1.place(relx=0.4,rely=0.4, relwidth=0.35, relheight=0.1)

    password2 = Label(frame, text="Confirm Password")
    password2.place(relx=0.4, rely=0.6, relwidth=0.35, relheight=0.1)

    password1 = Entry(frame, show="*")
    password1.place(relx=0.4, rely=0.6, relwidth=0.35, relheight=0.1)


root = Tk()
root.title("Form")
root.geometry("%dx%d" % (HEIGHT, WIDHT))
root.resizable(False, False)

root.option_add("*Font", "Helvetica")
root.option_add("*Background", "")

img = PhotoImage(file="bg3.gif")
background_label = Label(root, image=img)
background_label.place(relwidth=1, relheight=1)

button_singup = Button(root, text="SIGN IN", bg="gold")
button_singup.place(relx=0.2, rely=0.1, relwidth=0.3)

button_singup = Button(root, text="SIGN UP", bg="gold", command=reg)
button_singup.place(relx=0.5, rely=0.1, relwidth=0.3)
root.mainloop()