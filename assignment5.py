# # Database
# # 1. Create a table in your remote database named “dogs” with three
# # columns all NN (not null):
# # • VARCHAR (40) – name
# # • INT – age
# # • VARCHAR (30) – breed
# #
# create table dogs
# (
# 	name varchar(40) not null,
# 	age int not null,
# 	breed varchar(30) not null
# );

# # 2. Insert 3 dogs entries with different values
# #
# import pymysql
# conn = pymysql.connect(host='remotemysql.com',port=3306,user='pF3IWeqcGm',passwd='NxesvVNzBj',db='pF3IWeqcGm')
# # Getting a cursor from Database
# conn.autocommit(True)
# cursor = conn.cursor()
# cursor.execute("INSERT into pF3IWeqcGm.dogs (name, age, breed) VALUES ('NehNeh', 1, 'Lab')")
# cursor.execute("INSERT into pF3IWeqcGm.dogs (name, age, breed) VALUES ('Shep', 2, 'German')")
# cursor.execute("INSERT into pF3IWeqcGm.dogs (name, age, breed) VALUES ('FooFoo', 11, 'Mix')")
# cursor.close()
# conn.close()
#conn.commit()

# # 3. Update second dog age to any other age
# #
import pymysql
conn = pymysql.connect(host='remotemysql.com',port=3306,user='pF3IWeqcGm',passwd='NxesvVNzBj',db='pF3IWeqcGm')
# Getting a cursor from Database
conn.autocommit(True)
cursor = conn.cursor()
cursor.execute("UPDATE pF3IWeqcGm.dogs SET age = 34 WHERE name = 'Shep' ")

cursor.close()
conn.close()

# # 4. Delete the third dog from table
# #
# import pymysql
# conn = pymysql.connect(host='remotemysql.com',port=3306,user='pF3IWeqcGm',passwd='NxesvVNzBj',db='pF3IWeqcGm')
# # Getting a cursor from Database
# conn.autocommit(True)
# cursor = conn.cursor()
# cursor.execute("DELETE FROM pF3IWeqcGm.dogs WHERE age = 34 ")
#
# cursor.close()
# conn.close()

# # 5. Query table and print all dogs names.
# #
# def dog_list():
#     import pymysql
#     import json
#     conn = pymysql.connect(host='remotemysql.com',port=3306,user='pF3IWeqcGm',passwd='NxesvVNzBj',db='pF3IWeqcGm')
# # Getting a cursor from Database
#     conn.autocommit(True)
#     cursor = conn.cursor()
#     cursor.execute("select * FROM pF3IWeqcGm.dogs ")
#
#     dogs_json = []
#
#     for dog in cursor:
#         dogs_json.append(dog)
#     print(dogs_json)
#     cursor.close()
#     conn.close()
#     return json.dumps(dogs_json)
#
# dg = dog_list()
# # **Once database was created on remote, creating the table and
# # adding the columns can be done from MySQL workbench
# #
# # **Clauses 2-5 will must be done from code.
#
# Rest API
# 1.
# A. Get ILS to USD currency from any Currency converter API using
# requests module
# B. Print: “Please enter an amount of Shekeles to convert to Dollars”
# C. Print the result (amount * currency).
# Example: 3.5 shekels equals 1 dollars:
# If user enters the number 2 the output will be 7.
#
# #https://exchangeratesapi.io/
# import requests
#
# res =  requests.get("https://api.exchangeratesapi.io/latest?base=USD")
# data = res.json()
# results = data['rates']
# currency_value = results['ILS']
# num = float(input('Please enter an amount of Shekeles to convert to Dollars: '))
#
# print("The converted amount is: ", (num * currency_value))


# 2.
# Create a Flask application with the route /dogs (e.g: localhost:5000/dogs)
# which will return all dogs data (name, age, breed) from dogs table
# (from the database assignment at the top of this document).
# Class example can be used:
# https://github.com/Dgotlieb/Python-RestApi/blob/master/requests_test/rest_test.py
#
# from flask import Flask, request
# #
# app = Flask(__name__)
# #
# def dog_list():
#     import pymysql
#     import json
#     conn = pymysql.connect(host='remotemysql.com',port=3306,user='pF3IWeqcGm',passwd='NxesvVNzBj',db='pF3IWeqcGm')
# # Getting a cursor from Database
#     conn.autocommit(True)
#     cursor = conn.cursor()
#     cursor.execute("select * FROM pF3IWeqcGm.dogs ")
#
#     dogs_json = []
#
#     for dog in cursor:
#         dogs_json.append(dog)
#     print(dogs_json)
#     cursor.close()
#     conn.close()
#     return json.dumps(dogs_json)
#
# users = {}
# # supported methods
# @app.route('/dogs/', methods=['GET'])
# def dogs():
#     if request.method == 'GET':
#         return dog_list(), 200 # status code
#
#     elif request.method == 'POST':
#         # getting the json data payload from request
#         request_data = request.json
#         # treating request_data as a dictionary to get a specific value from key
#         user_name = request_data.get('user_name')
#         users[user_id] = user_name
#         return {'user id': user_id , 'user name': user_name, 'status': 'saved'}, 200 # status code
#   # todo elif for put and delete
#
#
# app.run(host='127.0.0.1', debug=True, port=5000)
# #
# #


# Extra:
# Add another route to your Flask application /add_dog which will get
# dogs data (name, age, breed) from POST (json) data.
# For example: {“name”: “rexi”, “age”:2, “breed”: “husky”}

from flask import Flask, request, jsonify, make_response

#
app = Flask(__name__)
#
def dog_list():
    import pymysql
    import json
    conn = pymysql.connect(host='remotemysql.com',port=3306,user='pF3IWeqcGm',passwd='NxesvVNzBj',db='pF3IWeqcGm')
# Getting a cursor from Database
    conn.autocommit(True)
    cursor = conn.cursor()
    cursor.execute("select * FROM pF3IWeqcGm.dogs ")

    dogs_json = []

    for dog in cursor:
        dogs_json.append(dog)
    print(dogs_json)
    cursor.close()
    conn.close()
    return json.dumps(dogs_json)

def dog_save(dn,da,db):
    import pymysql
    import json
    conn = pymysql.connect(host='remotemysql.com',port=3306,user='pF3IWeqcGm',passwd='NxesvVNzBj',db='pF3IWeqcGm')
# Getting a cursor from Database
    conn.autocommit(True)
    cursor = conn.cursor()
    dn = '"' + dn + '"'
    da = '"' + da + '"'
    db = '"' + db + '"'
    ins = 'insert into pF3IWeqcGm.dogs (name, age, breed) VALUES ('+ dn +','+ da + ','+ db +')'
    cursor.execute(ins)

    cursor.close()
    conn.close()


# supported methods
@app.route('/dogs/', methods=['GET'])
def dogs():
        return dog_list(), 200 # status code

@app.route('/add_dog', methods=['POST'])
def add_entry():
    if request.method == 'POST':
        # getting json data payload from request to add a dog
        if request.is_json:
            request_json = request.get_json()
            # treating request_data as a dictionary to get a specific value from key
            # {“name”: “rexi”, “age”:2, “breed”: “husky”}
            dog_name = request_json.get('name')
            dog_age = request_json.get('age')
            dog_breed = request_json.get('breed')
            dog_save(dog_name,dog_age,dog_breed)
            #print(request_json)
            return {'dog named': dog_name,'status': 'saved'}, 200  # status code
        else:
            # The request body wasn't JSON so return a 400 HTTP status code
            return "Request was not JSON", 400
        #return {'user id': user_id , 'user name': user_name, 'status': 'saved'}, 200 # status code


app.run(host='127.0.0.1', debug=True, port=5000)
#
#
