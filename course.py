import tkinter as tk
from tkinter import messagebox
import pyodbc


class Database:
    def __init__(self):
        self.conn = pyodbc.connect(
            "Driver={SQL Server Native Client 11.0};"
            "Server=CoT-CIS3365-09.cougarnet.uh.edu;"
            "Port=1433;"
            "Database=SoundboxDB;"
            "Trusted_Connection=no;"
            "UID=bchi2;"
            "PWD=Qwer123$;"
        )
        self.cursor = self.conn.cursor()
        # self.cur.execute(
        #     "CREATE TABLE IF NOT EXISTS parts (id INTEGER PRIMARY KEY, part text, customer text, retailer text, price text)")
        # self.conn.commit()

    def fetch(self):
        self.cursor.execute("SELECT * FROM Course")
        rows = self.cursor.fetchall()

        return rows

    def insert(self, employeeid, studentid, genreid, coursepriceid, coursenumberid, course_name, course_date,
               course_time):
        self.cursor.execute("INSERT INTO Course (employeeid, studentid, genreid, coursepriceid, coursenumberid, "
                            "course_name, course_date,course_time) VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
                            (employeeid, studentid, genreid, coursepriceid, coursenumberid, course_name, course_date,
                             course_time))
        self.conn.commit()

    def remove(self, courseid):
        self.cursor.execute("DELETE FROM Course WHERE courseid=?", (courseid,))
        self.conn.commit()

    def update(self, courseid, employeeid, studentid, genreid, coursepriceid, coursenumberid, course_name, course_date,
               course_time):
        self.cursor.execute("UPDATE Course SET employeeid = ?, studentid = ?, genreid = ?, coursepriceid = ?, "
                            "coursenumberid = ?, course_name = ?, course_date = ?, course_time = ? WHERE courseid = ?",
                            (employeeid, studentid, genreid, coursepriceid,
                             coursenumberid, course_name, course_date, course_time, courseid))
        self.conn.commit()

    def __del__(self):
        self.conn.close()


db = Database()


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
        self.course_name_text = tk.StringVar()
        self.course_name_label = tk.Label(
            self.master, text='Course Name', font=('bold', 12))
        self.course_name_label.grid(row=1, column=2, sticky=tk.W)
        self.course_name_entry = tk.Entry(self.master, textvariable=self.course_name_text)
        self.course_name_entry.grid(row=1, column=3)
        # Course Date
        self.course_date_text = tk.StringVar()
        self.course_date_label = tk.Label(
            self.master, text='Course Date', font=('bold', 12))
        self.course_date_label.grid(row=1, column=4, sticky=tk.W)
        self.course_date_entry = tk.Entry(self.master, textvariable=self.course_date_text)
        self.course_date_entry.grid(row=1, column=5)
        # Course Time
        self.course_time_text = tk.StringVar()
        self.course_time_label = tk.Label(
            self.master, text='Course Time', font=('bold', 12))
        self.course_time_label.grid(row=1, column=6, sticky=tk.W)
        self.course_time_entry = tk.Entry(self.master, textvariable=self.course_time_text)
        self.course_time_entry.grid(row=1, column=7)

        # Courses list (listbox)
        self.courses_list = tk.Listbox(self.master, height=25, width=150, border=0)
        self.courses_list.grid(row=3, column=0, columnspan=7,
                             rowspan=15, pady=20, padx=20)
        # Create scrollbar
        self.scrollbar = tk.Scrollbar(self.master)
        self.scrollbar.grid(row=3, column=7)
        # Set scrollbar to courses
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

    def select_item(self, event):
        try:
            # Get index
            index = self.courses_list.curselection()[0]
            # Get selected item
            self.selected_item = self.courses_list.get(index)

            # Display data at entry box
            self.employeeid_entry.delete(0, tk.END)
            self.employeeid_entry.insert(tk.END, self.selected_item[1])
            self.studentid_entry.delete(0, tk.END)
            self.studentid_entry.insert(tk.END, self.selected_item[2])
            self.genreid_entry.delete(0, tk.END)
            self.genreid_entry.insert(tk.END, self.selected_item[3])
            self.coursepriceid_entry.delete(0, tk.END)
            self.coursepriceid_entry.insert(tk.END, self.selected_item[4])
            self.coursenumberid_entry.delete(0, tk.END)
            self.coursenumberid_entry.insert(tk.END, self.selected_item[5])
            self.course_name_entry.delete(0, tk.END)
            self.course_name_entry.insert(tk.END, self.selected_item[6])
            self.course_date_entry.delete(0, tk.END)
            self.course_date_entry.insert(tk.END, self.selected_item[7])
            self.course_time_entry.delete(0, tk.END)
            self.course_time_entry.insert(tk.END, self.selected_item[8])
        except IndexError:
            pass

    # Add new item to the DB
    def add_item(self):
        if self.employeeid_text.get() == '' or self.studentid_text.get() == '' or self.genreid_text.get() == '' \
                or self.coursepriceid_text.get() == '' or self.coursenumberid_text.get() == '' \
                or self.course_name_text.get() == '' or self.course_date_text.get() == '' \
                or self.course_time_text.get() == '':
            messagebox.showerror('Required Fields', 'Please input all required fields.')
            return

        # Insert into our database
        db.insert(self.employeeid_text.get(), self.studentid_text.get(), self.genreid_text.get(),
                  self.coursepriceid_text.get(), self.coursenumberid_text.get(), self.course_name_text.get(),
                  self.course_date_text.get(), self.course_time_text.get())

        # Clear the list
        self.courses_list.delete(0, tk.END)
        # Insert new record into the list
        self.courses_list.insert(tk.END, (self.employeeid_text.get(), self.studentid_text.get(), self.genreid_text.get(),
                  self.coursepriceid_text.get(), self.coursenumberid_text.get(), self.course_name_text.get(),
                  self.course_date_text.get(), self.course_time_text.get()))
        self.clear_text()
        self.populate_list()

    def remove_item(self):
        db.remove(self.selected_item[0])
        self.clear_text()
        self.populate_list()

    def update_item(self):
        db.update(self.selected_item[0], self.employeeid_text.get(), self.studentid_text.get(), self.genreid_text.get(),
                  self.coursepriceid_text.get(), self.coursenumberid_text.get(), self.course_name_text.get(),
                  self.course_date_text.get(), self.course_time_text.get())
        self.clear_text()
        self.populate_list()

    def clear_text(self):
        self.employeeid_entry.delete(0, tk.END)
        self.studentid_entry.delete(0, tk.END)
        self.genreid_entry.delete(0, tk.END)
        self.coursepriceid_entry.delete(0, tk.END)
        self.coursenumberid_entry.delete(0, tk.END)
        self.course_name_entry.delete(0, tk.END)
        self.course_date_entry.delete(0, tk.END)
        self.course_time_entry.delete(0, tk.END)

    def populate_list(self):
        # Clear old item so that records doesn't double populate
        self.courses_list.delete(0, tk.END)

        # iterate through the data returned by the fetch method in Database Class
        for row in db.fetch():
            line = [row.courseid, row.employeeid, row.studentid, row.genreid, row.coursepriceid, row.coursenumberid, row.course_name,
                    row.course_date, row.course_time]
            self.courses_list.insert(tk.END, line)


root = tk.Tk()
app = Application(master=root)
app.mainloop()