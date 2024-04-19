'''
Q1. Design a function that will take a whole number and
prints the number and prints whether it is odd or not
'''
#def evenodd(number: int):
def evenodd():
    number = int(input('Pick a number: '))
    
    if number % 2:
        print('odd')
    else:
        print('even')
        
evenodd()

'''
Q2. Design a function that takes two numbers and prints
the smallest value.  Do not use the builtin min function.
'''
#def smallint(number1: int, number2: int):
def smallint():
    number1 = int(input('choose first number: '))
    number2 = int(input('choose second number: '))
    if number1 > number2:
        print(number2)
    else:
        print(number1)
smallint()

'''
Q3. Design a function that takes one argument: a person's age
and determines and prints the cost of
riding the bus based on that given age.
Your function should assume age is not negative.

If age is less than 18, the cost is $1.50.
If age is 65 or more, the cost is $2.00.
For all other values of age, the cost is $2.50.
'''
youth = 1.50
adult = 2.50
elder = 2.00
#def busfair(age: int):
def busfair():
    age = int(input('what is your age? '))
    
    if age >= 65:
        print(f'{elder:1.2f}')
    elif age < 18 and age > 0:
        print(f'{youth:1.2f}')
    else:
        print(f'{adult:1.2f}')
        
busfair()

'''
Q4. Design a function that takes a number within the range of 1 through 10.
The function should assume it will only be called with numbers 1 to 10.
The function should display the Roman numeral version of that number.
The following list shows the Roman numerals for the numbers 1 through 10:

Number:	Roman Numeral
1	I
2	II
3	III
4	IV
5	V
6	VI
7	VII
8	VIII
9	IX
10	X
'''

#def roman(num: int):
def roman():
    num = int(input('pick a number between 1 and 10: '))
    
    if num > 0 and num < 11:
        
            match num:
                case 1:
                    print('I')
                case 2:
                    print('II')
                case 3:
                    print('III')
                case 4:
                    print('IV')
                case 5:
                    print('V')
                case 6:
                    print('VI')
                case 7:
                    print('VII')
                case 8:
                    print('VIII')
                case 9:
                    print('XI')
                case 10:
                    print('X')
    else:
            print('You did not choose a number between 1 and 10')
        
roman()
            
        