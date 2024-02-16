# Author    Raymond Harrison
#
# Purpose   Python challenge
#
# tested    ver. 3.11.7 on Windows 11

import sqlite3
from sqlite3 import *

# making variable for tuples
fifthEle = (('Jean-Baptiste Zorg','Human', 122),('Korben Dallas','Meat Popsicle', 100),("Ak'not",'Mangalore',-5))

# Creating conn to RAM database
conn = sqlite3.connect(':memory:')

# creating function to use RAM database and make table
def create_connection():
    c = conn.cursor()
    c.execute("CREATE TABLE Roster(Name TEXT, Species TEXT, IQ INT)")
    conn.commit()

    # Insert values into table Roster
    c.executemany("INSERT INTO Roster VALUES (?,?,?)",fifthEle)
    conn.commit()

    # Update value in table
    c.execute("UPDATE Roster SET Species = ? WHERE Name = ?",('Human', 'Korben Dallas'))
    conn.commit()

    # Display names and IQ of all species 'Human'
    c.execute("SELECT * FROM Roster WHERE Species = 'Human'")
    rows = c.fetchall()
    for row in rows:
        print(row)






if __name__ == '__main__':
    create_connection()
