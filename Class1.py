#ex 1
age = input('enter your age:')
if int(age) > 18:
    print('Adult')
# ex 2
password = '12345'
upassword = input('enter your password:')
if password == upassword:
    print('Loggegin')
else:
    print('acces denied')

# ex 3
age = input('enter your age:')
hight = input('enter your hight:')

if (int(age) > 12 and int(hight) > 160):
    print('OK')
else:
    print('Forbidden')



