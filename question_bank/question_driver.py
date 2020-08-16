import tkinter as tk
import os.path

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))


#Method to save new questions to file
def writeFile():
    file = open("questions2.txt","a+")
    if people.get() == 1:
        file.write('\n'+"People"+'\t'+question_entry.get()+'\t'+answer_entry.get()+'\t')
    elif events.get() == 1:
        file.write('\n'+"Events"+'\t'+question_entry.get()+'\t'+answer_entry.get()+'\t')
    elif places.get() == 1:
        file.write('\n'+"Places"+'\t'+question_entry.get()+'\t'+answer_entry.get()+'\t')
    elif independence.get() == 1:
        file.write('\n'+"Independence Day"+'\t'+question_entry.get()+'\t'+answer_entry.get()+'\t')
    file.close()
    
def openFile():
    with open("questions2.txt", "r") as f:
        question_label = tk.Label(question_frame, text=f.read())
        question_label.grid(row=15)
        
    
        
        
def clearQuestions():
    question_frame.grid_forget()
    
    
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

question_frame = tk.Frame(question_bank)
question_frame.grid(row=15)

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

clear_button = tk.Button(question_bank)
clear_button.config(text = "Clear Questions", command = clearQuestions)
clear_button.grid(row=10)


question_bank.mainloop()