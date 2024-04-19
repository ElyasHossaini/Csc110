from cmath import cos
PST = 0.07
GST = 0.05

test_variable = 100

#def print_bill(price: float):
def print_bill():
    price = float(input('Enter price: '))
    """ print the bill breakdown for an item of given price
    >>> print_bill(0)
    item:	$   0.00
    PST:	$   0.00
    GST:	$   0.00
    total:	$   0.00
    >>> print_bill(43.99)
    item:	$  43.99
    PST:	$   3.08
    GST:	$   2.20
    total:	$  49.27
    """
    pst_charge = price * PST
    gst_charge = price * GST
    total = price + pst_charge + gst_charge

    print(f'item:  ${price:1.2f}')
    print(f'PST:   ${pst_charge:1.2f}')
    print(f'GST:   ${gst_charge:1.2f}')
    print(f'total: ${total:1.2f}')

print_bill()
'''
Q1a. The function definition above is a solution to the problem I left you
with at the end of last lecture.
Fix it so the prices to print to 2 decimal places.
'''

'''
Q1b.
If I uncomment each of the following lines what will the output be?
'''
# print_bill(43.99)
'''
item:  $43.99
PST:   $3.08
GST:   $2.20
total: $49.27
'''
# print(GST)
'''
0.05
'''
# print(PST)
'''
0.07
'''
#print(pst_charge)
'''
error, no value
'''
# print(gst_charge)
'''
error, no value
'''

'''
Q2a. What is the output if the function foo is called?
Documentation and type hints ommitted for demonstration purposes.
Q2b. What happens if we remove the following line from foo: test_variable = 1
it will error, there is no value to output

Q2c. What happens if we remove the following line from bar: x = 5.5
it will error, no value to output
'''


def foo():
    '''
    prints out in foo: 4.5 1
    >>>in foo: 4.5 1
    '''
    x = 4.5
    test_variable = 1
    bar()
    print('in foo:', x, test_variable)


def bar():
    global test_variable
    test_variable = 500
    x = 5.5
    print('in bar:', x, test_variable)


'''
Q3. What is the output if the function baz is called
Documentation and type hints ommitted for demonstration purposes.
'''


def goo(y):
    x = 5.5
    y += 2
    print('in goo:', x, y)


def baz():
    '''
    it will output goo and its own baz
    >>>in goo: 5.5 6.5
    in baz: 4.5 10
    '''
    x = 4.5
    y = 10
    goo(x)
    print('in baz:', x, y)

baz()
'''
Q4. Design a function that takes a temperature in Celcius as a whole number
and calculates the corresponding temperature in Farenheit
and prints the result rounded down to the nearest whole number
Recall: degrees farenheit = 9 / 5 * degrees celcius + 32
'''
#def farneheit_calculator(celcius: int):
def farenheit_calculator():
    celcius = int(input('Enter temprature in degrees celcius: '))
    farenheit = (9 / 5 * celcius + 32) // 1
    print('Temprature is:', farenheit)
    
farenheit_calculator()
    


'''
Q5. Design a function that takes the length of the hypotenuse of a right angle
triangle and one of the non-90 degree angle measurements in the triangle.
The function should calculate the length of side adjacent to the given angle
and print the result to the screen.

RECALL: cos(angle in degrees) = adjacent / hypotenuse

You will want to use the cos function from the math library!
Use the help function to find the documentation for math.cos
and remember to import the math library
by adding the following line to the top of this file:
import math

RECALL: 1 degree = PI/180 radians
Use the dir function to see what other useful functions
the math module has by typing dir(math) in your shell
NOTE: the math module also has a radians function that you can use
instead of using the formula above to convert degrees to radians!

here is a calculator to help you come up with examples for testing:
https://www.calculator.net/right-triangle-calculator.html
'''
#def adjacent_solver(hypotenuse: float, length: float):
degree = 3.14/180
def adjacent_solver():
    hypotenuse = float(input('Enter hypotenuse length: '))
    angle = float(input('Enter angle: '))
    
    adjacent = cos(angle * degree) * hypotenuse
    
    print(f'adjacent length is: {adjacent:1.2f}')
    
adjacent_solver()

'''
Q6. Design a function that takes an item weight in kilograms and
calculates the corresponding weight in pounds and prints the
result with 2 decimal places on the screen.
We assume a conversion rate of 2.2 pounds per kilogram.
'''
#def One_kilogram(kilo: float):
One_kilogram = 2.2
def kilo_to_lbs():
    kilo = float(input('Enter the weight in kilograms: '))
    
    lbs = kilo * One_kilogram
    
    print(f'The weigth in lbs is : {lbs:1.2f}')
    
kilo_to_lbs()