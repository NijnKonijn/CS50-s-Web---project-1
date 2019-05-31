#How to Connect Python and SQL Server
import pyodbc



conn = pyodbc.connect("Driver = {SQL Server Native Client 11.0};"               
               "Server = WEAZ-PS-API006\SQL2016;"
               "Database = U4salaris;"
               "username = Systeem;"
               "password = Unit4systeem;"
               "Trusted_Connection = yes;")

cursor = conn.cursor()


cursor.execute('SELECT * *')
# cursor.execute('SELECT * FROM Employ')



for row in cursor:
    print('row = %r' % (row,))


    # Leo Overvoorde
    # Patrick Vogelzang
    # Oproepkracht uren op 0 --> minder dan 5 aan