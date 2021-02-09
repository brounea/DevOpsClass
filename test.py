def my_func():
 try:
     my_file = open("words.txt", "r", encoding='utf-8')
     content = my_file.read()
     print(content)
     my_file.close()
 except IOError as e :
     print(e)


my_func()