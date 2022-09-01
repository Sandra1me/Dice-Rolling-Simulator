from tkinter import *
from PIL import ImageTk,Image
import random

#Define functions
def rollDice(img):
    chose=random.choice(img)
    dice=Label(image=chose)
    dice.grid(row=0,column=0, rowspan=3, columnspan=3, padx=20,pady=20)


#Create the window
root=Tk()
root.title('Dice Rolling Simulator')
root.resizable(0,0)

#Create images
n1=ImageTk.PhotoImage(Image.open("images/n1.png"))
n2=ImageTk.PhotoImage(Image.open("images/n2.png"))
n3=ImageTk.PhotoImage(Image.open("images/n3.png"))
n4=ImageTk.PhotoImage(Image.open("images/n4.png"))
n5=ImageTk.PhotoImage(Image.open("images/n5.png"))
n6=ImageTk.PhotoImage(Image.open("images/n6.png"))
img=[n1,n2,n3,n4,n5,n6]

#Create the label for the dice
aux=Label(root,width=40, height=15)
aux.grid(row=0,column=0, rowspan=3, columnspan=3, padx=20,pady=20)

#Create the roll button
roll=Button(root,text="Roll the dice!", command=lambda:rollDice(img), bg='#D9B1A3', fg='#BF0436')
roll.grid(row=4,column=0,pady=15)

#Create exit button
exitButton=Button(root,text="Exit",command=root.destroy, padx=15, bg='#D9D5A0', fg='#898C35')
exitButton.grid(row=4,column=2)

root.mainloop()
