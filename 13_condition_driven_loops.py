'''
Q1. Design a function called get_number that asks a
user to enter a whole number int >= 0 returns
the number as an integer.
TIP: remember the int function
'''
def get_number() -> int:
    num = int(input('pick a number: '))
    if num < 0:
        return 0
    else:
        return num


'''
Q2. update the get_number so that if the user enters
an invalid int (non-integer or number<0)
it repeatedly prompts the user.
When a valid entry is finally made, the function
returns the number as an integer
TIP: remember the isdigit function
'''
def get_number2() -> int:
    num = int(input('pick number: '))
    while num < 0:
        num = int(input('pick number: '))
    return num

'''
Q3. Design a function that will compute and return the sum of a series
of positive numbers entered by a user.  The user enters the values,
one at a time, and enters 0 to indicate there are no more values to enter.
If the user enters an invalid entry (non-integer or number<0),
they are repeatedly prompted until they enter valid data.
'''
def series() -> int:
    total = 0
    num = int(input('pick a number: '))
    while num != 0:
        total += num
        num = int(input('pick a number: '))
    return (total)

'''
Q4. Design a function that will determine and return the largest of a
series of positive numbers entered by a user.  The user enters the values,
one at a time, and enters 0 to indicate there are no more values to enter.
If the user enters an invalid entry (non-integer or number<0),
they are repeatedly prompted until they enter valid data.
'''
def return_largest() -> int:
    num = 1
    while num != 0:
        num1 = int(input('pick a number: '))
        if num1 == 0:
            break
        elif num < num1:
            num = num1
        
            
            
        
    return print(num)
    

'''
Q5. Design a function that will calculate and return the average of a
series of positive numbers entered by a user.  The user enters the values,
one at a time, and enters 0 to indicate there are no more values to enter.
If the user enters an invalid entry (non-integer or number<0),
they are repeatedly prompted until they enter valid data.
If the first number entered by the user is 0, the message
"Error: no data" is printed and the function returns -1.
'''
def seriesaverage() -> int:
    total = 0
    ticker = 0
    num = int(input('pick a number: '))
    while num != 0:
        total += num
        ticker += 1
        num = int(input('pick a number: '))
    return print(total/ticker)

