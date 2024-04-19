import doctest
import math
ADULT = 18
SENIOR = 65
CHILD_RATE = 1.50
ADULT_RATE = 2.50
SENIOR_RATE = 2.00

NUM_BUNS_PER_PACK = 8
NUM_DOGS_PER_PACK = 12

'''
Q1. You were asked to design a function that determines the cost of
riding the bus based on the value of the argument age of type int.
If age is less than 18, the cost is $1.50.
If age is 65 or more, the cost is $2.00.
For all other values of age, the cost is $2.50.

A friend of yours submitted the following code but was deducted marks for:
-inappropriate use of branching constructs
-redundant Boolean expressions
-magic numbers
-insufficient test coverage
-missing units in output

Edit the function in light of the feedback from the marker.
'''


def print_fare(age: int):
    """ determines the bus fare for a rider of the given age and prints it

    Precondition: age > 0
    >>> print_fare(15)
    The fare is: 1.50
    """
    if age < 18:
        fare = 1.50
    if age >= 65:
        fare = 2.00
    if age >= 18 and age < 65:
        fare = 2.50

    print(f'The fare is: {fare:.2f}')

#edited version
youth = 1.50
adult = 2.50
elder = 2.00
def busfair():
    age = int(input('what is your age? '))
    
    if age >= 65:
        print(f'{elder:1.2f}')
    elif age < 18 and age > 0:
        print(f'{youth:1.2f}')
    else:
        print(f'{adult:1.2f}')
        
#busfair()

'''
Q2. The following function design fails some of the given
example tests but there is more than one problem with it.
Find and fix the problems.
'''


def print_roman_numeral(num: int):
    """ determines and prints the corresponding roman numeral for the given num

    >>> print_roman_numeral(1)
    I
    >>> print_roman_numeral(2)
    II
    >>> print_roman_numeral(3)
    III
    >>> print_roman_numeral(4)
    IV
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
    if num == 2:
        roman_numeral = 'II'
    if num == 3:
        roman_numeral = 'III'
    if num == 4:
        roman_numeral = 'IV'
    if num == 6:
        roman_numeral = 'VI'
    if num == 7:
        roman_numeral = 'VII'
    if num == 8:
        roman_numeral = 'VIII'
    if num == 9:
        roman_numeral = 'IX'
    else:
        roman_numeral = 'X'

    print(roman_numeral)

#edited version
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
        
#roman()
'''
Q3. Design a function that takes 2 numbers representing an (x,y) point on a
graph and prints what quadrant it is in.  RECALL:  quadrants are numbered
1 through 4 counter clockwise starting at the upper right quadrant.

The function should print: '(x# , y#)' where x# and y# are the x,y arguments
if x and y are zero it should then print 'at center'
otherwise if x or y are zero it should print which axis it is on:
'on x-axis' or 'on y-axis'
otherwise it should print 'Q#' where # is the quadrant number it is in
'''
def quadrant_count():
    x = float(input('Whats x: '))
    y = float(input('whats y: '))
    
    if x > 0 and y > 0:
        print('in quadrant 1')
    elif x < 0 and y > 0:
        print('in quadrant 2')
    elif x < 0 and y < 0:
        print('in quadrant 3')
    elif x > 0 and y < 0:
        print('in quadrant 4')
    elif x == 0:
        print('on y axis')
    elif y == 0:
        print('on x axis')
    else:
        print('at center')
#quadrant_count()

'''
Q4. Design a function that takes two numbers:
one for air temperature (in degrees Celsius) and
one for air pressure(in pounds per square inch, psi) inside a mechanical device
The function should print the message "Error: data not valid",
if the pressure is negative, and then terminates
otherwise it should print a message about the machine's operation
according to the following:
If the temperature is above 300 degrees C or below 5 degrees C, or if the
pressure is above 150psi, the machine is not operating under normal conditions.

If the temperature is above 250 degrees C and the pressure is above 100psi,
the machine is not operating under normal conditions.
Otherwise, the machine is operating under normal conditions.

TIP: the temperature and pressure thresholds are all constant value
that should not change during your program.  How/where should you define them?
'''
def device():
    temp = float(input('what is temprature? '))
    pressure = float(input('what is pressure? '))
    
    if pressure < 0:
        print('Error: data not valid')
    elif temp > 300 or temp < 5 or pressure > 150:
        print('machine is not operating under normal conditions')
    elif temp > 250 and pressure > 100:
        print('machine is not operating under normal conditions')
    else:
        print('machine is operating under normal conditions')
#device()
        

'''
Q5. Write a function that takes the number of people coming
    to a picnic and prints the nubmer of packages of hot dogs and buns to buy
    assume: each person will eat 2 hot dogs and
    the number of buns in a package is NUM_BUNS_PER_PACK and
    the number of dogs in a package is NUM_DOGS_PER_PACK and
Tip: if you know you need 16 hot dogs and there are 8 buns per pack and
12 dogs per pack, you need to know how many whole bags of each you need,
plus an extra bag if the whole bags are not quite enough.
Think about how the results of the following expressions help:
16 // 8
16 % 8
16 // 12
16 % 12
'''
    
NUM_BUNS_PER_PACK = 8
NUM_DOGS_PER_PACK = 12

def picnic_shopping(num_people: int):
    # Calculate the total number of hot dogs and buns needed
    total_dogs_needed = num_people * 2
    total_buns_needed = num_people * 2

    # Calculate the number of whole packages needed, and if there's a remainder, add one extra package
    #math.ceil rounds up
    dog_packs_needed = math.ceil(total_dogs_needed / NUM_DOGS_PER_PACK)
    bun_packs_needed = math.ceil(total_buns_needed / NUM_BUNS_PER_PACK)

    # Print the results
    print(f"You will need to buy {dog_packs_needed} packages of hot dogs and {bun_packs_needed} packages of buns.")
    

        

        
