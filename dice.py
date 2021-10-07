import tkinter
from PIL import Image, ImageTk
import random


root = tkinter.Tk()
root.geometry('400x400')
root.title('Rolling dice')

BlankLine = tkinter.Label(root, text='')
BlankLine.pack()

HeadingLabel = tkinter.Label(root, text='Rolling Dice', 
    fg='light green', bg='dark green', font='Helvetica 16 bold italic')
HeadingLabel.pack()

dice = [
    r'dice_rolling\img\die1.png',
    r'dice_rolling\img\die2.png',
    r'dice_rolling\img\die3.png',
    r'dice_rolling\img\die4.png',
    r'dice_rolling\img\die5.png',
    r'dice_rolling\img\die6.png'
]

DiceImage = ImageTk.PhotoImage(Image.open(random.choice(dice)))

ImageLabel = tkinter.Label(root, image=DiceImage)
ImageLabel.image = DiceImage
ImageLabel.pack(expand=True)

def rolling_dice():
    DiceImage = ImageTk.PhotoImage(Image.open(random.choice(dice)))
    ImageLabel.configure(image=DiceImage)

button = tkinter.Button(root, text='Roll the dice', fg='blue', command=rolling_dice)
button.pack(expand=True)

root.mainloop()

# https://data-flair.training/blogs/dice-rolling-simulator-python/