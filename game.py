import random
from tkinter import *

root = Tk() 
root.title("Rolling dice simulation by Ashutosh") 
root.iconbitmap('icon.bmp') 
root.geometry('700x400')   

l1 = Label(root,text='',font=("times", 260))     

def roll_dice():
    number = ['\u2680','\u2681','\u2682','\u2683','\u2684','\u2685'] 
    l1.config(text=f'{random.choice(number)}{random.choice(number)}') 
    l1.pack() 

b1 = Button(root,text="Let's Roll",command=roll_dice) 
b1.place(x=330,y=10) 

root.mainloop() 