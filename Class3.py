# Jan -17 2021
# i/o

my_file = open("testfile.txt", "a+", encoding='utf-8')
my_file.seek(0) # set the file cursor to the begining
content = my_file.read()
print(content)
my_file.write("\nzvuv is gr8\n")
print(content)
my_file.close()

# carbage collection

# error handling
try:
    f = open("testfile.txt", "r", encoding='utf-8')

except IOError as e :
    print(e)
finally:
    print('this code will run always')
    f.close()
print('1')


# with statment
# nicer way to do the same thig as above (error handling)
with open("testfile.txt", "w", encoding='utf-8') as wfile:
    wfile.write('hi')

# naming conventions
# functions names are lower case can use "_" to separate words
# variable names lower case
# package names lower case
# installed flask by using locally on this project flask.

# https://github.com/Dgotlieb/PyFlask
# https://github.com/Dgotlieb/PySelenium

