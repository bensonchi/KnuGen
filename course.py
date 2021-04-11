import tkinter as tk
from tkinter import messagebox


class Application(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        master.title('Course Record')
        # Width height
        master.geometry("1150x650")
        # Create widgets/grid
        self.create_widgets()
        # Init selected item var
        self.selected_item = 0
        # Populate initial list
        self.populate_list()

    def create_widgets(self):
        # Employee ID
        self.part_text = tk.StringVar()
        self.part_label = tk.Label(
            self.master, text='Employee ID', font=('bold', 12), pady=20)
        self.part_label.grid(row=0, column=0, sticky=tk.W)
        self.part_entry = tk.Entry(self.master, textvariable=self.part_text)
        self.part_entry.grid(row=0, column=1)
        # Student ID
        self.customer_text = tk.StringVar()
        self.customer_label = tk.Label(
            self.master, text='Student ID', font=('bold', 12))
        self.customer_label.grid(row=0, column=2, sticky=tk.W)
        self.customer_entry = tk.Entry(
            self.master, textvariable=self.customer_text)
        self.customer_entry.grid(row=0, column=3)
        # Genre ID
        self.retailer_text = tk.StringVar()
        self.retailer_label = tk.Label(
            self.master, text='Genre ID', font=('bold', 12))
        self.retailer_label.grid(row=0, column=4, sticky=tk.W)
        self.retailer_entry = tk.Entry(
            self.master, textvariable=self.retailer_text)
        self.retailer_entry.grid(row=0, column=5)
        # Course Price ID
        self.price_text = tk.StringVar()
        self.price_label = tk.Label(
            self.master, text='Course Price ID', font=('bold', 12))
        self.price_label.grid(row=0, column=6, sticky=tk.W)
        self.price_entry = tk.Entry(self.master, textvariable=self.price_text)
        self.price_entry.grid(row=0, column=7)
        # Course Number ID
        self.price_text = tk.StringVar()
        self.price_label = tk.Label(
            self.master, text='Course Number ID', font=('bold', 12))
        self.price_label.grid(row=1, column=0, sticky=tk.W)
        self.price_entry = tk.Entry(self.master, textvariable=self.price_text)
        self.price_entry.grid(row=1, column=1)
        # Course Name
        self.price_text = tk.StringVar()
        self.price_label = tk.Label(
            self.master, text='Course Name', font=('bold', 12))
        self.price_label.grid(row=1, column=2, sticky=tk.W)
        self.price_entry = tk.Entry(self.master, textvariable=self.price_text)
        self.price_entry.grid(row=1, column=3)
        # Course Date
        self.price_text = tk.StringVar()
        self.price_label = tk.Label(
            self.master, text='Course Date', font=('bold', 12))
        self.price_label.grid(row=1, column=4, sticky=tk.W)
        self.price_entry = tk.Entry(self.master, textvariable=self.price_text)
        self.price_entry.grid(row=1, column=5)
        # Course Time
        self.price_text = tk.StringVar()
        self.price_label = tk.Label(
            self.master, text='Course Time', font=('bold', 12))
        self.price_label.grid(row=1, column=6, sticky=tk.W)
        self.price_entry = tk.Entry(self.master, textvariable=self.price_text)
        self.price_entry.grid(row=1, column=7)

        # Parts list (listbox)
        self.parts_list = tk.Listbox(self.master, height=25, width=150, border=0)
        self.parts_list.grid(row=3, column=0, columnspan=7,
                             rowspan=15, pady=20, padx=20)
        # Create scrollbar
        self.scrollbar = tk.Scrollbar(self.master)
        self.scrollbar.grid(row=3, column=7)
        # Set scrollbar to parts
        self.parts_list.configure(yscrollcommand=self.scrollbar.set)
        self.scrollbar.configure(command=self.parts_list.yview)

        # Bind select
        self.parts_list.bind('<<ListboxSelect>>', self.select_item)

        # Buttons
        self.add_btn = tk.Button(
            self.master, text="Add Part", width=12, command=self.add_item)
        self.add_btn.grid(row=2, column=0, pady=20)

        self.remove_btn = tk.Button(
            self.master, text="Remove Part", width=12, command=self.remove_item)
        self.remove_btn.grid(row=2, column=2)

        self.update_btn = tk.Button(
            self.master, text="Update Part", width=12, command=self.update_item)
        self.update_btn.grid(row=2, column=4)

        self.exit_btn = tk.Button(
            self.master, text="Clear Input", font=(12), width=12, command=self.clear_text)
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