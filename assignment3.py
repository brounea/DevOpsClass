# Assignment
#
# 1. Write the following code: a = 1/0;
#
# 2. Build a corresponding try-except block to
# try:
#     a = 1/0
# except ZeroDivisionError as e :
#     print(e)

# avoid exception.
#
# 3. Is the following code legal?
# yes this is legal - only issue was with the double quotes
# try :
#     x = 1
# finally :
#     print('finally')
#
# 4. What exception types can be caught by the
# following handler?
# Except:
# Answer
# the above Except is a spcial case since uppercase E could mean user defined exception.
#
# 5. What is wrong with using the above type of
# exception handler?
# Answer:
# The above Exception needs to be defined first before using it
#
# 6. What exceptions can be caught by the
# following handlers?
# ...
# except IOError ...
# It is an error raised when an input/output operation fails,
# such as the print statement or the open() function when trying to open a file that does not exist.
# It is also raised for operating system-related errors
# except ZeroDivisionError
# This  error is raised when the program is trying to devide by zero

# 7. Create a text file named “words.txt”
# programmatically
# 8. Write your name into the file
#
# try:
#     f = open("words.txt", "a", encoding='utf-8')
#     f.write('Arnon was here!')
#     f.close()
# except IOError as e :
#     print(e)

# 9. Read your file content and print it
# try:
#     my_file = open("words.txt", "r", encoding='utf-8')
#     content = my_file.read()
#     print(content)
#     my_file.close()
# except IOError as e :
#     print(e)

# 10. Write Hebrew content into your text file and
# try:
#     my_file = open("words.txt", "a", encoding='utf-8')
#     my_file.write('ארנון היה פה')
#     my_file.close()
# except IOError as e :
#     print(e)

# print its content programmatically.
#
# try:
#     my_file = open("words.txt", "r", encoding='utf-8')
#     content = my_file.read()
#     print(content)
#     my_file.close()
# except IOError as e :
#     print(e)

# 11. Create a Flask application which listens to
# port 30000 and has 2 routes:
#

#  /content - which returns the content of
# any txt file and status code 200
# (e.g: localhost:4000/content).
#  /register - which writes the word “hello”
# into any txt file and return “success” and
# status code 201 as a response
# (e.g: localhost:4000/register).
#
#
from flask import Flask
#
app = Flask(__name__)
print('the app is :' + app.env)
#
# # accessed via <HOST>:<PORT>/content
#
@app.route('/content')
def read_file_content():
     try:
         f = open('words.txt', 'r', encoding='utf-8')
         content = f.read()
         f.close()
     except IOError as e :
         print(e)
     return 'The file content is :' + content , 200 # status code

@app.route("/register")
def write_hello():
     try:
         my_file = open("words.txt", "a", encoding='utf-8')
         my_file.write('Hello')
         my_file.close()
     except IOError as e:
          print(e)
     return "Success", 201 # status code

app.run(host='127.0.0.1', debug=True, port=4000)
#
#
# Challenge:
# 12. Create an image from code (png file) Hint:
# use Pillow
#
# from PIL import Image, ImageDraw
#
# def code_to_img(fname):
#     with open(fname, "r", encoding='utf-8') as wfile:
#         content = wfile.read()
#         # file name for the new img
#         imgFile = fname[:-4] + '.png'
#
#         img = Image.new('RGB', (200, 60), color = (73, 109, 137))
#
#         d = ImageDraw.Draw(img)
#         d.text((10,40), content, fill=(255,255,0))
#         img.save(imgFile)
#
# code_to_img('testfile.txt')

