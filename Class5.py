#mysql
# Created!
# You have successfully created a new database. The details are below.
#
# Username: pF3IWeqcGm
#
# Database name: pF3IWeqcGm
#
# Password: NxesvVNzBj
#
# Server: remotemysql.com
#
# Port: 3306
#
# These are the username and password to log in to your database and phpMyAdmin

# pyMySql

import pymysql
conn = pymysql.connect(host='remotemysql.com',port=3306,user='pF3IWeqcGm',passwd='NxesvVNzBj',db='pF3IWeqcGm')
# Getting a cursor from Database
conn.autocommit(True)
cursor = conn.cursor()

# INSERT data into table
#cursor.execute("INSERT into pF3IWeqcGm.users (name, id) VALUES ('john', 5)")
#conn.commit()

# SELECT all data from table “users”
cursor.execute("SELECT * FROM pF3IWeqcGm.dogs;")

# UPDATE data inside the table
cursor.execute("UPDATE SCHEMA_NAME.users SET id = '10' WHERE name = 'john'")

# DELETE data from the table
cursor.execute("DELETE FROM SCHEMA_NAME.users WHERE name = 'john'")

# Iterating table and printing all users
for row in cursor:
    print(row)

cursor.close()
conn.close()