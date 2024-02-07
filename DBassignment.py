
import sqlite3

#connect to database
conn = sqlite3.connect('test1.db')

#create table for database
with conn:
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_filename(\
        ID INTEGER PRIMARY KEY AUTOINCREMENT, \
        col_fileName TEXT)")
    conn.commit()


conn = sqlite3.connect('test1.db')

# list of file names

fileList = ('information.docx', 'Hello.txt', 'myImage.png', \
            'myMovie.mpg', 'World.txt', 'data.pdf', 'myPhoto.jpg')

# for loop through each object to find files that end in .txt
for x in fileList:
    if x.endswith('txt'):
        with conn:
            cur = conn.cursor()
            #insert only .txt files into table
            cur.execute("INSERT INTO tbl_filename(col_fileName) VALUES (?)",(x,))
            print(x)

conn.close()
