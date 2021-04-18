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
        self.cursor.execute("SELECT * FROM StudentCourseStatus")
        rows = self.cursor.fetchall()

        return rows

    def insert(self, studentid, courseid, studentcategoryid, studentcodedid, student_course_status):
        self.cursor.execute("INSERT INTO StudentCourseStatus (studentid, courseid, studentcategoryid, studentcodeid, "
                            "student_course_status) VALUES (?, ?, ?, ?, ?)",
                            (studentid, courseid, studentcategoryid, studentcodedid, student_course_status))
        self.conn.commit()

    def remove(self, studentcoursestatusid):
        self.cursor.execute("DELETE FROM StudentCourseStatus WHERE studentcoursestatusid=?", (studentcoursestatusid,))
        self.conn.commit()

    def update(self, studentcoursestatusid, studentid, courseid, studentcategoryid, studentcodeid, student_course_status):
        self.cursor.execute("UPDATE StudentCourseStatus SET studentid = ?, courseid = ?, studentcategoryid = ?, "
                            "studentcodeid = ?, student_course_status = ? WHERE studentcoursestatusid = ?",
                            (studentid, courseid, studentcategoryid, studentcodeid, student_course_status,
                             studentcoursestatusid))
        self.conn.commit()

    def __del__(self):
        self.conn.close()


db = Database()


class Application(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        master.title('Student Course Status')
        # Width height
        master.geometry("1100x650")
        # Create widgets/grid
        self.create_widgets()
        # Init selected item var
        self.selected_item = 0
        # Populate initial list
        self.populate_list()

    def create_widgets(self):
        # Student ID
        self.studentid_text = tk.StringVar()
        self.studentid_label = tk.Label(
            self.master, text='Student ID', font=('bold', 12), pady=20)
        self.studentid_label.grid(row=0, column=0, sticky=tk.W)
        self.studentid_entry = tk.Entry(
            self.master, textvariable=self.studentid_text)
        self.studentid_entry.grid(row=0, column=1)
        # Course ID
        self.courseid_text = tk.StringVar()
        self.courseid_label = tk.Label(
            self.master, text='Course ID', font=('bold', 12))
        self.courseid_label.grid(row=0, column=2, sticky=tk.W)
        self.courseid_entry = tk.Entry(
            self.master, textvariable=self.courseid_text)
        self.courseid_entry.grid(row=0, column=3)
        # Student Category ID
        self.studentcategoryid_text = tk.StringVar()
        self.studentcategoryid_label = tk.Label(
            self.master, text='Student Category ID', font=('bold', 12))
        self.studentcategoryid_label.grid(row=0, column=4, sticky=tk.W)
        self.studentcategoryid_entry = tk.Entry(
            self.master, textvariable=self.studentcategoryid_text)
        self.studentcategoryid_entry.grid(row=0, column=5)
        #  Student Code ID
        self.studentcodeid_text = tk.StringVar()
        self.studentcodeid_label = tk.Label(
            self.master, text='Student Code ID', font=('bold', 12))
        self.studentcodeid_label.grid(row=1, column=0, sticky=tk.W)
        self.studentcodeid_entry = tk.Entry(self.master, textvariable=self.studentcodeid_text)
        self.studentcodeid_entry.grid(row=1, column=1)
        # Student Course Status
        self.student_course_status_text = tk.StringVar()
        self.student_course_status_label = tk.Label(
            self.master, text='Student Course Status', font=('bold', 12))
        self.student_course_status_label.grid(row=1, column=2, sticky=tk.W)
        self.student_course_status_entry = tk.Entry(self.master, textvariable=self.student_course_status_text)
        self.student_course_status_entry.grid(row=1, column=3)


        # listbox
        self.studentCourseStatus_list = tk.Listbox(self.master, height=25, width=150, border=0)
        self.studentCourseStatus_list.grid(row=3, column=0, columnspan=7,
                             rowspan=15, pady=20, padx=20)
        # Create scrollbar
        self.scrollbar = tk.Scrollbar(self.master)
        self.scrollbar.grid(row=3, column=7)
        # Set scrollbar to courses
        self.studentCourseStatus_list.configure(yscrollcommand=self.scrollbar.set)
        self.scrollbar.configure(command=self.studentCourseStatus_list.yview)
        # Bind select
        self.studentCourseStatus_list.bind('<<ListboxSelect>>', self.select_item)

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
            index = self.studentCourseStatus_list.curselection()[0]
            # Get selected item
            self.selected_item = self.studentCourseStatus_list.get(index)

            # Display data at entry box
            self.studentid_entry.delete(0, tk.END)
            self.studentid_entry.insert(tk.END, self.selected_item[1])
            self.courseid_entry.delete(0, tk.END)
            self.courseid_entry.insert(tk.END, self.selected_item[2])
            self.studentcategoryid_entry.delete(0, tk.END)
            self.studentcategoryid_entry.insert(tk.END, self.selected_item[3])
            self.studentcodeid_entry.delete(0, tk.END)
            self.studentcodeid_entry.insert(tk.END, self.selected_item[4])
            self.student_course_status_entry.delete(0, tk.END)
            self.student_course_status_entry.insert(tk.END, self.selected_item[5])
        except IndexError:
            pass

    # Add new item to the DB
    def add_item(self):
        if self.studentid_text.get() == '' or self.courseid_text.get() == '' or self.studentcategoryid_text.get() == '' \
                or self.studentcodeid_text.get() == '' or self.student_course_status_text.get() == '':
            messagebox.showerror('Required Fields', 'Please input all required fields.')
            return

        # Insert into our database
        db.insert(self.studentid_text.get(), self.courseid_text.get(), self.studentcategoryid_text.get(),
                  self.studentcodeid_text.get(), self.student_course_status_text.get())
        # Clear the list
        self.studentCourseStatus_list.delete(0, tk.END)
        # Insert new record into the list
        self.studentCourseStatus_list.insert(tk.END, (self.studentid_text.get(), self.courseid_text.get(),
                                                      self.studentcategoryid_text.get(), self.studentcodeid_text.get(),
                                                      self.student_course_status_text.get()))
        self.clear_text()
        self.populate_list()

    def remove_item(self):
        db.remove(self.selected_item[0])
        self.clear_text()
        self.populate_list()

    def update_item(self):
        db.update(self.selected_item[0], self.studentid_text.get(), self.courseid_text.get(),
                  self.studentcategoryid_text.get(), self.studentcodeid_text.get(),
                  self.student_course_status_text.get())
        self.clear_text()
        self.populate_list()

    def clear_text(self):
        self.studentid_entry.delete(0, tk.END)
        self.courseid_entry.delete(0, tk.END)
        self.studentcategoryid_entry.delete(0, tk.END)
        self.studentcodeid_entry.delete(0, tk.END)
        self.student_course_status_entry.delete(0, tk.END)

    def populate_list(self):
        # Clear old item so that records doesn't double populate
        self.studentCourseStatus_list.delete(0, tk.END)

        # iterate through the data returned by the fetch method in Database Class
        for row in db.fetch():
            line = [row.studentcoursestatusid, row.studentid, row.courseid, row.studentcategoryid, row.studentcodeid,
                    row.student_course_status]
            self.studentCourseStatus_list.insert(tk.END, line)


root = tk.Tk()
app = Application(master=root)
app.mainloop()