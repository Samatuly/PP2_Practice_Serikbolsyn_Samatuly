import psycopg2
conn = psycopg2.connect("dbname=postgres user=postgres password=Serik2004")
cur = conn.cursor()
datas = [
    ('Serikbolsyn', '87714105109'),
    ('Azamat', '87015697859'), 
    ('Kairat', '87075123699'),
    ('Bakdaulet', '87012223344'),
    ('Timur', '87775698740')
]
# to update phone if user already exists
'''
add_name = str(input("Add a name: "))
add_number = str(input("Add a number: "))
for i in datas:
    if(add_name == i[0]):
        change_permission = str(input("'%s' has in your phonebook. Do you want to update phone?: " % (add_name)))
        if(change_permission == "Yes") or (change_permission == "yes") or (change_permission == "YES"):
            cur.execute("Update phonebook set phone = '%s' where name= '%s'" % (add_number, i[0]))
        elif(change_permission == "No") or (change_permission == "no") or (change_permission == "NO"):
            continue
conn.commit()
conn.close()
'''
# to add multiple users to phonebook
cur.executemany("Insert into phonebook(name, phone) values (%s, %s)", datas)
conn.commit()
conn.close()

# to delete row by username
'''
delete_name = str(input("Write a name, which you want to delete: "))
cur.execute("Delete from phonebook where name = '%s'" % (delete_name))
conn.commit()
conn.close()
'''
# limit function
'''
cur.execute("SELECT * from phonebook LIMIT 1;")
print(cur.fetchall())
'''
# offset function
'''
cur.execute("SELECT * from phonebook OFFSET 1;")
print(cur.fetchall())
'''