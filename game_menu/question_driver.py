import tkinter as tk
import os.path


class QuestionBank:
    def __init__(self, master):
        self.master = master
        master.title("Question Bank")
        master.geometry("200x300")


        self.menubar = tk.Menu(master)
        self.filemenu = tk.Menu(self.menubar, tearoff=0)
        self.filemenu.add_command(label="View Questions", command=self.openFile)
        self.filemenu.add_separator()
        self.filemenu.add_command(label="Exit", command=master.quit)
        self.menubar.add_cascade(label="File", menu=self.filemenu)

        master.config(menu=self.menubar)
        
        self.question_frame = tk.Frame(master)
        self.question_frame.grid(row=15)

        self.people = tk.IntVar()
        self.events = tk.IntVar()
        self.places = tk.IntVar()
        self.independence = tk.IntVar()

        self.people_check = tk.Checkbutton(master, text="People", variable=self.people, onvalue=1, offvalue=0).grid(row=0)
        self.events_check = tk.Checkbutton(master, text="Events", variable=self.events, onvalue=1, offvalue=0).grid(row=1)
        self.places_check = tk.Checkbutton(master, text="Places", variable=self.places, onvalue=1, offvalue=0).grid(row=2)
        self.independence_check = tk.Checkbutton(master, text="Independence Day", variable=self.independence, onvalue=1, offvalue=0).grid(row=3)

        self.q = tk.StringVar()  # question
        self.question_label = tk.Label(master, text="Enter Question").grid(row=4)
        self.question_entry = tk.Entry(master, textvariable=self.q)
        self.question_entry.grid(row=5)

        self.a = tk.StringVar()  # answer
        self.answer_label = tk.Label(master, text="Enter Answer").grid(row=6)
        self.answer_entry = tk.Entry(master, textvariable=self.a)
        self.answer_entry.grid(row=7)

        self.write_button = tk.Button(master)
        self.write_button.config(text="Save Question", command=self.writeFile)
        self.write_button.grid(row=8)

        self.view_button = tk.Button(master)
        self.view_button.config(text="View Questions", command=self.openFile)
        self.view_button.grid(row=9)

        self.clear_button = tk.Button(master)
        self.clear_button.config(text="Clear Questions", command=self.clearQuestions)
        self.clear_button.grid(row=10)

        self.game_board_button = tk.Button(master)
        self.game_board_button.config(text="Game Board", command=self.openGame)
        self.game_board_button.grid(row=11)


    #Method to launch and run game_board file
    def openGame(self):
        os.system("python game_board_test.py")

    #Method to save new questions to file
    def writeFile(self):
        file = open("questions2.txt","a+")
        if self.people.get() == 1:
            file.write('\n'+"People"+'\t'+self.question_entry.get()+'\t'+self.answer_entry.get()+'\t')
        elif self.events.get() == 1:
            file.write('\n'+"Events"+'\t'+self.question_entry.get()+'\t'+self.answer_entry.get()+'\t')
        elif self.places.get() == 1:
            file.write('\n'+"Places"+'\t'+self.question_entry.get()+'\t'+self.answer_entry.get()+'\t')
        elif self.independence.get() == 1:
            file.write('\n'+"Independence Day"+'\t'+self.question_entry.get()+'\t'+self.answer_entry.get()+'\t')
        file.close()

    def openFile(self):
        with open("questions2.txt", "r") as f:
            self.question_label = tk.Label(self.question_frame, text=f.read())
            self.question_label.grid(row=15)


    def clearQuestions(self):
        self.question_frame.grid_forget()
        self.__init__(root)


__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
root = tk.Tk()
my_gui = QuestionBank(root)
root.mainloop()