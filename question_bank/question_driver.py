import tkinter as tk
import os.path

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

def writeFile():
    file = open("test.txt","a+")
    file.write('\n' + question_entry.get() + ' / ' + answer_entry.get())
    file.close()
    
def openFile():
    with open("questions.txt", "r") as f:
        tk.Label(question_bank, text=f.read()).grid(row=15)
    
    
question_bank = tk.Tk()
question_bank.title("Question Bank")
question_bank.geometry("200x300")

menubar = tk.Menu(question_bank)
filemenu = tk.Menu(menubar, tearoff=0)
filemenu.add_command(label="Open", command=openFile)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=question_bank.quit)
menubar.add_cascade(label="File", menu=filemenu)

question_bank.config(menu=menubar)

people = tk.IntVar()
events = tk.IntVar()
places = tk.IntVar()
independence = tk.IntVar()

tk.Checkbutton(question_bank, text = "People", variable = people, onvalue = 1, offvalue = 0).grid(row=0)
tk.Checkbutton(question_bank, text = "Events", variable = events, onvalue = 1, offvalue = 0).grid(row=1)
tk.Checkbutton(question_bank, text = "Places", variable = places, onvalue = 1, offvalue = 0).grid(row=2)
tk.Checkbutton(question_bank, text = "Independence Day", variable = independence, onvalue = 1, offvalue = 0).grid(row=3)


q = tk.StringVar() # question
question_label = tk.Label(question_bank, text = "Enter Question").grid(row=4)
question_entry = tk.Entry(question_bank, textvariable = q)
question_entry.grid(row=5)


a = tk.StringVar() # answer
answer_label = tk.Label(question_bank, text = "Enter Answer").grid(row=6)
answer_entry = tk.Entry(question_bank, textvariable = a)
answer_entry.grid(row=7)


write_button = tk.Button(question_bank)
write_button.config(text = "Save Question", command = writeFile)
write_button.grid(row=8)

view_button = tk.Button(question_bank)
view_button.config(text = "View Questions", command = openFile)
view_button.grid(row=9)


question_bank.mainloop()