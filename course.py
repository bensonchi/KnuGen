import tkinter as tk
from tkinter import messagebox


class Application(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        master.title('Course Record')
        # Width height
        master.geometry("1100x650")
        # Create widgets/grid
        self.create_widgets()
        # Init selected item var
        self.selected_item = 0
        # Populate initial list
        self.populate_list()

    def create_widgets(self):
        # Employee ID
        self.employeeid_text = tk.StringVar()
        self.employeeid_label = tk.Label(
            self.master, text='Employee ID', font=('bold', 12), pady=20)
        self.employeeid_label.grid(row=0, column=0, sticky=tk.W)
        self.employeeid_entry = tk.Entry(self.master, textvariable=self.employeeid_text)
        self.employeeid_entry.grid(row=0, column=1)
        # Student ID
        self.studentid_text = tk.StringVar()
        self.studentid_label = tk.Label(
            self.master, text='Student ID', font=('bold', 12))
        self.studentid_label.grid(row=0, column=2, sticky=tk.W)
        self.studentid_entry = tk.Entry(
            self.master, textvariable=self.studentid_text)
        self.studentid_entry.grid(row=0, column=3)
        # Genre ID
        self.genreid_text = tk.StringVar()
        self.genreid_label = tk.Label(
            self.master, text='Genre ID', font=('bold', 12))
        self.genreid_label.grid(row=0, column=4, sticky=tk.W)
        self.genreid_entry = tk.Entry(
            self.master, textvariable=self.genreid_text)
        self.genreid_entry.grid(row=0, column=5)
        # Course Price ID
        self.coursepriceid_text = tk.StringVar()
        self.coursepriceid_label = tk.Label(
            self.master, text='Course Price ID', font=('bold', 12))
        self.coursepriceid_label.grid(row=0, column=6, sticky=tk.W)
        self.coursepriceid_entry = tk.Entry(self.master, textvariable=self.coursepriceid_text)
        self.coursepriceid_entry.grid(row=0, column=7)
        # Course Number ID
        self.coursenumberid_text = tk.StringVar()
        self.coursenumberid_label = tk.Label(
            self.master, text='Course Number ID', font=('bold', 12))
        self.coursenumberid_label.grid(row=1, column=0, sticky=tk.W)
        self.coursenumberid_entry = tk.Entry(self.master, textvariable=self.coursenumberid_text)
        self.coursenumberid_entry.grid(row=1, column=1)
        # Course Name
        self.coursename_text = tk.StringVar()
        self.coursename_label = tk.Label(
            self.master, text='Course Name', font=('bold', 12))
        self.coursename_label.grid(row=1, column=2, sticky=tk.W)
        self.coursename_entry = tk.Entry(self.master, textvariable=self.coursename_text)
        self.coursename_entry.grid(row=1, column=3)
        # Course Date
        self.coursedate_text = tk.StringVar()
        self.coursedate_label = tk.Label(
            self.master, text='Course Date', font=('bold', 12))
        self.coursedate_label.grid(row=1, column=4, sticky=tk.W)
        self.coursedate_entry = tk.Entry(self.master, textvariable=self.coursedate_text)
        self.coursedate_entry.grid(row=1, column=5)
        # Course Time
        self.coursetime_text = tk.StringVar()
        self.coursetime_label = tk.Label(
            self.master, text='Course Time', font=('bold', 12))
        self.coursetime_label.grid(row=1, column=6, sticky=tk.W)
        self.coursetime_entry = tk.Entry(self.master, textvariable=self.coursetime_text)
        self.coursetime_entry.grid(row=1, column=7)

        # Courses list (listbox)
        self.courses_list = tk.Listbox(self.master, height=25, width=150, border=0)
        self.courses_list.grid(row=3, column=0, columnspan=7,
                             rowspan=15, pady=20, padx=20)
        # Create scrollbar
        self.scrollbar = tk.Scrollbar(self.master)
        self.scrollbar.grid(row=3, column=7)
        # Set scrollbar to parts
        self.courses_list.configure(yscrollcommand=self.scrollbar.set)
        self.scrollbar.configure(command=self.courses_list.yview)

        # Bind select
        self.courses_list.bind('<<ListboxSelect>>', self.select_item)

        # Buttons
        self.add_btn = tk.Button(
            self.master, text="Add Record", font=11, width=13, command=self.add_item)
        self.add_btn.grid(row=2, column=0, pady=20)

        self.remove_btn = tk.Button(
            self.master, text="Remove Record", font=11, width=13, command=self.remove_item)
        self.remove_btn.grid(row=2, column=2)

        self.update_btn = tk.Button(
            self.master, text="Update Record", font=11, width=13, command=self.update_item)
        self.update_btn.grid(row=2, column=4)

        self.exit_btn = tk.Button(
            self.master, text="Clear Input", font=11, width=13, command=self.clear_text)
        self.exit_btn.grid(row=2, column=6)

    def select_item(self):
        print('SELECT')

    def add_item(self):
        print('ADD')

    def remove_item(self):
        print('REMOVE')

    def update_item(self):
        print('UPDATE')

    def clear_text(self):
        print('CLEAR')

    def populate_list(self):

        print('POPULATE')

root = tk.Tk()
app = Application(master=root)
app.mainloop()