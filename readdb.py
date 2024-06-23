#https://stackoverflow.com/questions/35677592/read-db-file-into-python
#You will need to iterate over all the tables and convert to list. This is completely untested code, but should give you an idea of what you need to do:

import sqlite3
def importdb(db):
     conn = sqlite3.connect(db)
     c = conn.cursor()
     c.execute("SELECT name FROM sqlite_master WHERE type='table';")
     for table in c.fetchall()
         yield list(c.execute('SELECT * from ?;', (table[0],)))
