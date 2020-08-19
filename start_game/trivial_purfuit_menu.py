import tkinter as tk
from PIL import Image, ImageTk
from itertools import count
import os.path

class ImageLabel(tk.Label):
    """a label that displays images, and plays them if they are gifs"""
    def load(self, im):
        if isinstance(im, str):
            im = Image.open(im)
        self.loc = 0
        self.frames = []

        try:
            for i in count(1):
                self.frames.append(ImageTk.PhotoImage(im.copy()))
                im.seek(i)
        except EOFError:
            pass

        try:
            self.delay = im.info['duration']
        except:
            self.delay = 100

        if len(self.frames) == 1:
            self.config(image=self.frames[0])
        else:
            self.next_frame()

    def unload(self):
        self.config(image="")
        self.frames = None

    def next_frame(self):
        if self.frames:
            self.loc += 1
            self.loc %= len(self.frames)
            self.config(image=self.frames[self.loc])
            self.after(self.delay, self.next_frame)

#Function to launch and run the file for the question bank
def questionBank():
    root.destroy() #close existing gui before opening next
    os.chdir("../question_bank/")
    os.system("python3 question_driver.py")

#Function to launch and run the file for the game board
def openGame():
    root.destroy() #close existing gui before opening next
    os.chdir("../gameplay/")
    os.system("python3 game_board.py")

#Test GUI for functionality to show gif
root = tk.Tk()
root.title("Welcome to Trivial Purfuit!") #set title of window
lbl = ImageLabel(root) #create image label in the gui window
__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
lbl.pack()
lbl.load('trivialpurfuit.gif') #load gif into gui window

#Create a button that links to method for running question bank
bank_button = tk.Button(root)
bank_button.config(text="Launch the Question Bank", command=questionBank)
bank_button.pack(side="left")

#Create a button that links to method for running game board
game_button = tk.Button(root)
game_button.config(text="Launch the Game Board", command=openGame)
game_button.pack(side="right")

#run mainloop to launch gui
root.mainloop()