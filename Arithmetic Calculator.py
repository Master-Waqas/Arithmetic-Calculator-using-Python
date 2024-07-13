#Simple Arithematic Calculator

first_number = int(input('Enter 1st Number : '))
second_number = int(input('Enter 2nd Number : '))
opt = input('Enter Option +, -, *, / : ')

if opt == '+':
    print('Result : ', first_number + second_number)

elif opt == '-':
    print('Result : ', first_number - second_number)

elif opt == '*':
    print('Result : ', first_number * second_number)

elif opt == '/':
    print('Result : ', first_number / second_number)

else:
    print('Error : Enter Correct Option.')