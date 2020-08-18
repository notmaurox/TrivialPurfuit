from tkinter import *
from tkinter import messagebox
import tkinter as tk
import os.path

#Class Question Bank - add, save, view questions
class QuestionBank:
    def __init__(self, master):
        self.master = master
        master.title("Question Bank")
        master.geometry("1100x900")

        #Create a file menu that will be used for program navigation
        self.menubar = tk.Menu(master)
        self.filemenu = tk.Menu(self.menubar, tearoff=0)
        #Menu option to view questions in question bank
        self.filemenu.add_command(label="View Questions", command=self.openFile)
        #Menu option to launch game board
        self.filemenu.add_command(label="Launch Game Board", command=self.openGame)
        self.filemenu.add_separator()
        #Menu option to quit the program
        self.filemenu.add_command(label="Exit", command=master.quit)
        #Rename menu 'navigation'
        self.menubar.add_cascade(label="Navigation", menu=self.filemenu)
        master.config(menu=self.menubar)

        #Create a new frame below the buttons that will display questions
        self.question_frame = tk.Frame(master)
        self.question_frame.grid(row=15, sticky='w')

        #Create int variable (1 or 0) for the category selection for adding questions
        self.people = tk.IntVar()
        self.events = tk.IntVar()
        self.places = tk.IntVar()
        self.independence = tk.IntVar()

        #Using the int variables, create check buttons for the various categories a user can select
        self.people_check = tk.Checkbutton(master, text="People", variable=self.people, onvalue=1, offvalue=0).grid(row=0, sticky='w')
        self.events_check = tk.Checkbutton(master, text="Events", variable=self.events, onvalue=1, offvalue=0).grid(row=1, sticky='w')
        self.places_check = tk.Checkbutton(master, text="Places", variable=self.places, onvalue=1, offvalue=0).grid(row=2, sticky='w')
        self.independence_check = tk.Checkbutton(master, text="Independence Day", variable=self.independence, onvalue=1, offvalue=0).grid(row=3, sticky='w')

        #Create a string variable for user to input a question
        self.q = tk.StringVar()  # question
        self.question_label = tk.Label(master, text="Enter Question").grid(row=4, sticky='w')
        self.question_entry = tk.Entry(master, textvariable=self.q)
        self.question_entry.grid(row=5, sticky='w')

        #Create a string variable for user to input an answer
        self.a = tk.StringVar()  # answer
        self.answer_label = tk.Label(master, text="Enter Answer").grid(row=6, sticky='w')
        self.answer_entry = tk.Entry(master, textvariable=self.a)
        self.answer_entry.grid(row=7, sticky='w')

        #Button created that accesses writeFile() to save user input to .txt that contains questions
        self.write_button = tk.Button(master)
        self.write_button.config(text="Save Question", command=self.writeFile)
        self.write_button.grid(row=8, sticky='w')

        #Button created that accesses openFile() and views questions in their own frame
        self.view_button = tk.Button(master)
        self.view_button.config(text="View Questions", command=self.openFile)
        self.view_button.grid(row=9, sticky='w')

        #Button created that accesses clearQuestions() which destroys the frame and resets the gui
        self.clear_button = tk.Button(master)
        self.clear_button.config(text="Clear Questions", command=self.clearQuestions)
        self.clear_button.grid(row=10, sticky='w')

    #Method to launch and run game_board file
    def openGame(self):
        root.destroy() #close existing gui before launching new one
        os.system("python game_board_test.py")

    #Method to save new questions to file
    def writeFile(self):
        file = open("questions2.txt","a+")
        #Based on which box is selected, the appropriate category is written to the file
        if (self.people.get() + self.events.get() + self.places.get() + self.independence.get()) != 1:
            #if more or less than 1 checkbox is selected, give an error
            messagebox.showinfo(title="Warning", message="Must exactly one category")
            self.__init__(root)  # reset gui after warning
        elif self.people.get() == 1:
            file.write('\n'+"People"+'\t'+self.question_entry.get()+'\t'+self.answer_entry.get()+'\t')
            self.__init__(root)  # reset gui after saving
        elif self.events.get() == 1:
            file.write('\n'+"Events"+'\t'+self.question_entry.get()+'\t'+self.answer_entry.get()+'\t')
            self.__init__(root)  # reset gui after saving
        elif self.places.get() == 1:
            file.write('\n'+"Places"+'\t'+self.question_entry.get()+'\t'+self.answer_entry.get()+'\t')
            self.__init__(root)  # reset gui after saving
        elif self.independence.get() == 1:
            file.write('\n'+"Independence Day"+'\t'+self.question_entry.get()+'\t'+self.answer_entry.get()+'\t')
            self.__init__(root)  # reset gui after saving
        file.close()


    #Method to open .txt and display in separate frame in GUI window
    def openFile(self):
        with open("questions2.txt", "r") as f:
            self.question_label = tk.Label(self.question_frame, text=f.read(), anchor='w')
            self.question_label.grid(row=15, sticky='w')

    #Method to clear the grid displaying questions and reset the gui
    def clearQuestions(self):
        self.question_frame.grid_forget()
        self.__init__(root) #reset gui after clearing the question frame


root = tk.Tk()
questionGUI = QuestionBank(root)

root.mainloop()