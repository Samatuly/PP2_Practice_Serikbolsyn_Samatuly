import psycopg2
conn = psycopg2.connect("dbname=postgres user=postgres password=Serik2004")
cur = conn.cursor()
cur.execute("SELECT * from students")
records = cur.fetchall()
print(records)

# delete function
'''
def del_name(name):
    conn = psycopg2.connect("dbname=postgres user=postgres password=Serik2004")
    cur = conn.cursor()
    cur.execute("Delete from students where name='%s'" % name)
    conn.commit()
    conn.close()

del_name("Timur")
'''
# change function
'''
def change_name(name):
    conn = psycopg2.connect("dbname=postgres user=postgres password=Serik2004")
    cur = conn.cursor()
    cur.execute("Update students set name='Bakdaulet' where name='%s'" % name)
    conn.commit()
    conn.close()

change_name("Ospan")
'''
# add function
'''
name_input = str(input())
phone_input = int(input())
def insert_name(name, phone):
    conn = psycopg2.connect("dbname=postgres user=postgres password=Serik2004")
    cur = conn.cursor()
    cur.execute("Insert into public.students(name, phone) values('%s', '%s')" % (name, phone))
    conn.commit()
    conn.close()

insert_name(name_input, phone_input)
'''
# import function
'''
def import_name():
    conn = psycopg2.connect("dbname=postgres user=postgres password=Serik2004")
    cur = conn.cursor()
    cur.execute("Copy students(name, phone) from '%s' delimiters ',' csv header;" % r'C:\Users\Orynb\Desktop\Serikbolsyn\python\Lab10\information.csv')
    conn.commit()
    conn.close()

import_name()
'''