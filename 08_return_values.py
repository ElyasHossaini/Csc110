import doctest

ADULT = 18
SENIOR = 65
CHILD_RATE = 1.50
ADULT_RATE = 2.50
SENIOR_RATE = 2.00

'''
Q0. Design a function that will take two numbers and
returns the sum of those numbers
'''
def sum(x: int, y: int) -> int:
    return x + y


'''
Q0b. Design a function that will take two numbers and prints the average
of those numbers.
In your function body, call the funtion desiged in Q1a
to practice calling a function from another function.
'''
def average():
    sum1 = sum(6, 2)
    average = sum1 / 2
    print(average)


'''
Q0c. If the function you designed in Q0a printed the sum instead of
returning it, would you average function still behave as expected?
'''
#no because it wouldn't remember the value
'''
Q1. Below is the print_fare function we wrote in a past lecture.
Continuing in this problem domain, design a separate function that takes
the number of children, number of adults and number of seniors
and returns the total fare for those riders.
You function should take into acount a group discount of 10%
for groups of 10 or more.
You can assume the function will not be passed negative values.

NOTICE: print_fare does not return a value, so calling it will not be useful
BUT, there are CONSTANTS defined that might be useful!
'''


def print_fare(age: int) -> None:
    """ determines the bus fare for a rider of the given age and prints it
    Precondition: age > 0
    >>> print_fare(0)
    The fare is: $1.50
    >>> print_fare(ADULT-1)
    The fare is: $1.50
    >>> print_fare(ADULT)
    The fare is: $2.50
    >>> print_fare(ADULT+1)
    The fare is: $2.50
    >>> print_fare(SENIOR-1)
    The fare is: $2.50
    >>> print_fare(SENIOR)
    The fare is: $2.00
    >>> print_fare(SENIOR+1)
    The fare is: $2.00
    """
    fare = 0
    if age < ADULT:
        fare = CHILD_RATE
    elif age >= SENIOR:
        fare = SENIOR_RATE
    else:
        fare = ADULT_RATE

    print(f'The fare is: ${fare:.2f}')

def total(children: int, adult: int, senior: int) -> float:
    if children + adult + senior >= 10:
        totalmoney = (children * CHILD_RATE) + (adult * ADULT_RATE) + (senior * SENIOR_RATE)
        total = (totalmoney * 0.1) + totalmoney
        return total
    else:
        total = (children * CHILD_RATE) + (adult * ADULT_RATE) + (senior * SENIOR_RATE)
        return total


'''
Q2. design a function that takes the amount of money in a bank account and
the number of children, number of adults and number of seniors.
You can assume the function will not be passed negative values for
number of people, but the account balance can be negative.

The function should print the total fare for all of these people and
the balance left in the bank account after the fare is paid.
The function should return the balance left in the bank account
after the fare is paid.
'''
def bankaccount(bank: float) -> float:
    money = bank - total()
    return money



''' Q3. Recall we designed the following function in a past lecture.
Update this function so it does not print the roman numeral,
but instead returns it.'''


def print_roman_numeral(num: int) -> str:
    """ determines and prints the corresponding roman numeral for the given num
    Precondition: 1 <= num <=10
    >>> print_roman_numeral(1)
    I
    >>> print_roman_numeral(2)
    II
    >>> print_roman_numeral(3)
    III
    >>> print_roman_numeral(4)
    IV
    >>> print_roman_numeral(5)
    V
    >>> print_roman_numeral(6)
    VI
    >>> print_roman_numeral(7)
    VII
    >>> print_roman_numeral(8)
    VIII
    >>> print_roman_numeral(9)
    IX
    >>> print_roman_numeral(10)
    X
    """
    roman_numeral = ''

    if num == 1:
        roman_numeral = 'I'
    elif num == 2:
        roman_numeral = 'II'
    elif num == 3:
        roman_numeral = 'III'
    elif num == 4:
        roman_numeral = 'IV'
    elif num == 5:
        roman_numeral = 'V'
    elif num == 6:
        roman_numeral = 'VI'
    elif num == 7:
        roman_numeral = 'VII'
    elif num == 8:
        roman_numeral = 'VIII'
    elif num == 9:
        roman_numeral = 'IX'
    else:
        roman_numeral = 'X'

    return roman_numeral
