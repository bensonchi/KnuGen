import pyodbc 
# Some other example server values are
# server = 'localhost\sqlexpress' # for a named instance
# server = 'myserver,port' # to specify an alternate port

cnxn = pyodbc.connect(
                "Driver={SQL Server Native Client 11.0};"
                "Server=CoT-CIS3365-09.cougarnet.uh.edu;"
                "Port=1433;"
                "Database=SoundboxDB;"
                "Trusted_Connection=no;"
                "UID=bchi2;"
                "PWD=Qwer123$;"
            )
cursor = cnxn.cursor()

#Sample select query
cursor.execute("SELECT * FROM Course;")
row = cursor.fetchone()
while row:
    print(str(row[0])+' '+str(row[1])+' '+str(row[2]))

    row = cursor.fetchone()