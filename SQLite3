improt sqlite3              #if you don't have sqlite3 do(pip install -U sqlite3)
conn = sqlite3.connect('mydatabase.db')    #this to connect the database with python
#creating a table in database
conn.execute("""CREATE TABLE STUDENT(rollno int,name text,address text)""")
#inserting a vaule to the table STUDENT
conn.execute("""INSERT INTO STUDENT VAULES(1,'abc','india')""")
conn.commit()
#TO see the inserted records
see = conn.execute("""SELECT rollno,name,address FROM STUDENT """)
for row in see:
       print('rollno:',row[0])
       print('name:',row[1])
       print('address:',row[2])
 #To Update the record in the database
 
 conn.execute("""UPDATE STUDENT SET rollno=2 where name='abc' """)
 conn.commit()
 
 #To delete a record from the database
 
 conn.execute("""DELETE FROM STUDENT where name='abc' """)
 conn.commit()
 

