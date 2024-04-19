import doctest

'''
Q1. Design a function that takes an integer n and prints
print the squares of numbers from 0 to n separated by commas.
Your function should assume n is not negative.
'''
def squares(num: int) -> None:
    for i in range(num + 1):
        if i != num:
            print(i ** 2 , end = ",")
        else:
            print(i ** 2)
        

'''
Q2. Design a function that takes an integer n and returns
the sum of the squares of numbers from 0 to n.
Your function should assume n is not negative.
'''
def squares2(num: int) -> int:
    i = 0
    for number in range(num + 1):
        i += number ** 2
    return i
    
    

        

#***************
'''
Q3. Design a function that takes an integer n and returns
a string with the squares of all the numbers from 0 to limit inclusive,
where numbers are separated by commas.
'''
'''
IMPORTANT IMPORTANT IMPORTANT IMPORTANT IMPORTANT IMPORTANT IMPORTANT IMPORTANT
IMPORTANT IMPORTANT IMPORTANT IMPORTANT IMPORTANT IMPORTANT IMPORTANT IMPORTANT
IMPORTANT IMPORTANT IMPORTANT IMPORTANT IMPORTANT IMPORTANT IMPORTANT IMPORTANT
IMPORTANT IMPORTANT IMPORTANT IMPORTANT IMPORTANT IMPORTANT IMPORTANT IMPORTANT
IMPORTANT IMPORTANT IMPORTANT IMPORTANT IMPORTANT IMPORTANT IMPORTANT IMPORTANT
IMPORTANT IMPORTANT IMPORTANT IMPORTANT IMPORTANT IMPORTANT IMPORTANT IMPORTANT


THIS IS HOW TO ADD CAMAS OR SPACES BETWEEN STRINGS IN RETURN VALUE
MAKE AN EMPTY STRING
HAVE THAT EMPTY STRING += str(THING YOU WANT TO RETURN) + 'ITEM YOU WANT TO HAVE BETWEEN THINGS'
return result[:-1] TO GET THE RESULT WITHOUT FINAL CAMA OR WHATEVER 
'''
def stringsquare(num: int) -> list:
    result = ""

    # Loop through numbers from 0 to n
    for i in range(num+1):
        # Add square of the number followed by a comma to the string
        result += str(i**2) + ","
    
    # Remove the last comma from the string
    return print(result[:-1])
stringsquare(4)



'''
Q4. Design a function that takes an integer n and prints
prints the number n down to 1 followed by 'BLASTOFF!'
Your function should assume n is greater than 0.
'''
def rocket(num: int) -> None:
    for i in range(num, 0, -1):
        print(i)
    print('BLASTOFF!')
    

'''
Q5. Design a function that takes an integer n and a string and
prints that string n times with no additional spaces or newlines.
Your function should assume n is not negative
You cannot use the * operator.
'''
def stringmult(num: int, word: str) -> None:
    for i in range(num):
        print(word, end='')

#*************
'''
Q6. Design a function that takes an integer n and a string and
returns a new string that has the given string repeated n times
with no additional spaces or newlines.
Your function should assume n is not negative
You cannot use the * operator.
'''
def newstr(num: int, word: str) -> str:
    result = ''
    for i in range(num):
        result += word + ''
        return (word)
    
