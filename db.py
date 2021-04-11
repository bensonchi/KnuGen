import pyodbc

# Some other example server values are
# server = 'localhost\sqlexpress' # for a named instance
# server = 'myserver,port' # to specify an alternate port
#
# cnxn = pyodbc.connect(
#     "Driver={SQL Server Native Client 11.0};"
#     "Server=CoT-CIS3365-09.cougarnet.uh.edu;"
#     "Port=1433;"
#     "Database=SoundboxDB;"
#     "Trusted_Connection=no;"
#     "UID=bchi2;"
#     "PWD=Qwer123$;"
# )
# cursor = cnxn.cursor()
#
# # Sample select query
# cursor.execute("SELECT * FROM Course;")
# row = cursor.fetchone()
# while row:
#     print(str(row[0]) + ' ' + str(row[1]) + ' ' + str(row[2]))
#
#     row = cursor.fetchone()
#

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
        print(rows[0])
        print(type(rows[0]))
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
