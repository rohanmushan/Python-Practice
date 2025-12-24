from tkinter import *
from tkinter import messagebox
import random

def no():
    messagebox.showinfo(' ','Thanks Broo')
    messagebox.showinfo(' ','I already knew youre gay')
    quit()

def morionMouse(event):
    btnNO.place(x=random.randint(0, 500), y=random.randint (0,500))

root = Tk()
root.geometry('600x600')
root.title('survey')
root.resizable(width=False, height=False)
root['bg'] = 'white'
label = Label(root, text = 'Are you Gay?', font='Ariel 20 bold', bg='white')
label.pack()

btnNO = Button(root, text='NO', font='Arial 20 bold')
btnNO.place(x=170, y=100)
btnNO.bind('<Enter>', morionMouse)

btnYes = Button(root, text='Yes',font='Arial 20 bold', command=no)
btnYes.place(x=350, y=100)

root.mainloop()
