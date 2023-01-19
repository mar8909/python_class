#ifstatement-boolean
user_name = input('What is your name: ?')
age= int(input('How old are you? '))
if age >= 100:
    print("You are too old to sing up!")
elif age >= 18:
    print('You are now signed up!')
elif age < 0:
    print("you haven't born yet!")
else:
    print('You must put your age')

usuario = True

if usuario:
    print('You are online!')
else:
    print(('You are not online'))
