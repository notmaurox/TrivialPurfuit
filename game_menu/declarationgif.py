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

def questionBank():
    os.system("python question_driver.py")

def openGame(self):
    self.os.system("python game_board_test.py")

root = tk.Tk()
lbl = ImageLabel(root)
__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
lbl.pack()
lbl.load('trivialpurfuit.gif')

view_button = tk.Button(root)
view_button.config(text="Question Bank", command=questionBank)
view_button.pack()

#clear_button = tk.Button(root)
#clear_button.config(text="Game Board", command=openGame)
#clear_button.grid(row=10)


root.mainloop()