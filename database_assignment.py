    #imports sqlite3
import sqlite3

    #creates a variable to create the database
conn = sqlite3.connect('test2.db')

    #this makes it so you can start to execute commands
with conn:
    cur = conn.cursor()
    
    #this creates the table and columns 
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_files(\
        ID INTEGER PRIMARY KEY AUTOINCREMENT, \
        col_txtFiles TXT \
        )")
    conn.commit()
conn = sqlite3.connect('test2.db')
    #Creates the list of files we need loop through 
fileList = ('information.docx','Hello.txt','myImage.png', \
            'myMovie.mpg','World.txt','data.pdf','myPhoto.jpg')
    #Creates the loop that will find only the files ending with .txt
for x in fileList:
    if x.endswith('.txt'):
        with conn:
            cur = conn.cursor()
    #(x,)makes it a one element tuple for each file ending with .txt
            cur.execute("INSERT INTO tbl_files (col_txtFiles) VALUES (?)", (x,))
            print(x)


conn.close()

