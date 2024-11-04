
# Importing the necessary libraries such as tikinter and random
from tkinter import *
import tkinter as tk
import random
import time

# Setting up the window and its size
root = tk.Tk()
root.geometry("450x650")
root.title("Gambling Sim")

# Add image file 
bg = PhotoImage(file = 'hakari.ppm') 
bg2 = PhotoImage(file= 'gamble.ppm')
bg3 = PhotoImage(file='bgbg.ppm')
  
# Show image using label 
# label1 = Label( root, image = bg) 
# label1.place(relx=0.5, rely=0.9, anchor="center") 

# label2 = Label( root, image = bg2, ) 
# label2.place(relx=0.8, rely=0, anchor="center") 

label3 = Label(root, image=bg3)
label3.place(x=0,y=0)

# Define the deck of cards
suits = ["Clubs", "Diamonds", "Hearts", "Spades"]
ranks = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]
cols = ["Red", "Black"]

# Defining the variable of the amount of money the user starts with
global allowance
allowance = 100

global info

# Creating a function that randomly chooses a card
def randomize():
    global number
    global house
    global color
    number = random.choice(list(ranks))
    house = random.choice(list(suits))
    if house == "Hearts" or house == "Diamonds":
        color = "Red"
    else:
        color = "Black"

info = Label(root)

# Creating a function to see if the user got their guesses right
def checkGamble():


    global allowance
    global multiplier
    global warning
    global bet

    try:
        bet = int(amountBet.get())
    except ValueError:
        Label(root, text='Please enter a valid bet amount!', font=('Ariel', 18)).place(relx=0.5, rely=0.7, anchor="center")
        return
    
    if bet <= allowance:

        if numberVar.get() == number and houseVar.get() == house:
            multiplier = 5
            result_text = f'JACKPOT!!! You just got {(bet * multiplier) - bet} dollars!'
            allowance = round(allowance - int(amountBet.get()) + (bet * multiplier), 2)
            bankacount.config(text='$' + str(allowance))
        elif numberVar.get() == number:
            multiplier = 1.5
            result_text = f'Number! You just got {(bet * multiplier) - bet} dollars!'
            allowance = round(allowance - int(amountBet.get()) + (bet * multiplier), 2)
            bankacount.config(text='$' + str(allowance))
        elif houseVar.get() == house:
            multiplier = 1.25
            result_text = f'House! You just got {(bet * multiplier) - bet} dollars!'
            allowance = round(allowance - int(amountBet.get()) + (bet * multiplier), 2)
            bankacount.config(text='$' + str(allowance))
        elif colorVar.get() == color:
            multiplier = 1.1
            result_text = f'Color! You just got {((bet * multiplier) - bet):.2f} dollars!'
            allowance = round(allowance - int(amountBet.get()) + (bet * multiplier), 2)
            bankacount.config(text='$' + str(allowance))
        else:
            result_text = 'You lost this one! 99 percent of gamblers quit before their first win.' 
            allowance = allowance - bet
            bankacount.config(text='$' + str(allowance))

        info.config(text=result_text)
    
    else:
        warning = Label(root, text='Please enter a valid bet amount!', font=('Ariel', 18)).place(relx=0.5, rely=0.7, anchor="center")
        return

re = Label(root, text="", font=('Ariel', 20))


# Creating a function that tells the user the random card that was chosen.
def result():
    res = 'The card was a ' + color + ' ' + number + ' of ' + house
    re.config(text=res)


# 
def submitted():
    randomize()
    checkGamble()
    result()





title = Label(root, text='How much are you willing to invest', font=('Ariel', 25))
bankacount = Label(root, text='$' + str(round(allowance, 2)), font=('Ariel', 17))

amountBet=Entry(root)
colorVar = StringVar()
houseVar = StringVar()
numberVar = StringVar()

colorChosen = OptionMenu(root, colorVar, *cols, )
houseChosen = OptionMenu(root, houseVar, *suits, )
numberChosen = OptionMenu(root, numberVar, *ranks, )



info.place(relx=0.5,rely=0.6, anchor="center")

submit = Button(root, text='Submit', command=submitted, background="black", foreground="black", width=7, height=3)




# Carefully placed the UI in order to create the most visually appealing visuals
bankacount.place(relx=0.1, rely=0.05, anchor="center")
title.place(relx=0.5, rely=0.1, anchor="center")
amountBet.place(relx=0.5, rely=0.2, anchor="center")
colorChosen.place(relx=0.3, rely=0.3, anchor="center")
houseChosen.place(relx=0.5, rely=0.3, anchor="center")
numberChosen.place(relx=0.7, rely=0.3, anchor="center")
submit.place(relx=0.5, rely=0.5, anchor="center")
re.place(relx=0.5, rely=0.8, anchor="center")
root.mainloop()

