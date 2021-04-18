import pyodbc

class Database:
    def __init__(self):
        self.conn = pyodbc.connect(

            "Driver={SQL Server Native Client 11.0};"
            "Server=DESKTOP-NVFR9BM\SQLEXPRESS;"
            "Database=SoundboxDB;"
            "Trusted_Connection=yes;"
            "UID=bchi2;"
            "Pwd=Qwer123$;"
        )
        self.cursor = self.conn.cursor()
        # self.cur.execute(
        #     "CREATE TABLE IF NOT EXISTS parts (id INTEGER PRIMARY KEY, part text, customer text, retailer text, price text)")
        # self.conn.commit()

    def fetch(self):
        self.cursor.execute("select courseid, employeeid, studentid, genreid, coursepriceid, coursenumberid, "
                            "course_name ,course_date, course_time "
                            "from Course "
                            "where deleted = 0")
        rows = self.cursor.fetchall()
        for row in rows:
            print(row)
        return rows

    def insert(self, employeeid, studentid, genreid, coursepriceid, coursenumberid, course_name, course_date,
               course_time):
        self.cursor.execute("INSERT INTO Course (employeeid, studentid, genreid, coursepriceid, coursenumberid, "
                            "course_name, course_date,course_time) VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
                            (employeeid, studentid, genreid, coursepriceid, coursenumberid, course_name, course_date,
                             course_time))
        self.conn.commit()

    def remove(self, courseid):
        self.cursor.execute("UPDATE course SET deleted = 1 WHERE courseid = ?", (courseid,))
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
db.remove(3)
db.fetch()