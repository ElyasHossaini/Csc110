'''
Q0. The following code attempts to print the total price
of a group of items I would like to buy followed by
the amount of money I will have left in my wallet.
My wallet started with 200 dollars.
There are a few things wrong with this program.
What do you think is wrong and how would you fix it?
'''


print('total of item prices:', 3+4+6+14)
#add parenthesis to the total of item prices
print('wallet balance:', 200 - (3+4+6+14))


'''
Q1a. Recall from your math classes that the equation for
the lengths of the sides in a right triangle is:
  a^2 + b^2 = c^2
- using the ^ to indicate "raise to the power of" in the description
- how is "raise to the power of" represented in Python?

#with a **

Write the code that will print the length of side c of
a right triangle with side a length as 3 and side length b as 4.
'''

x = 3 ** 2 + 4 ** 2
print(x ** 0.5)

'''
Q1b. Update the program you just wrote so
it is contained within a function.
Test the function by calling it from the shell.
'''
def square_root():
    x = 3 ** 2 + 4 ** 2
    print(x ** 0.5)

square_root()

'''
Q1c. complete the function below so it prints the lengths
of all sides of the right triangle.
Try to avoid re-writing code you have already written!

Test the function by calling it from the shell.
Your output should look something like this...

Dimensions of this right triangle:
the short sides are length: 3 and 4
the hypotenuse is length:  5.0
'''


def print_right_triangle_dimensions():
    a = 3
    b = 4
    c = (a ** 2 + b ** 2) ** 0.5
    print("The short sides are", a, "and", b)
    print("The hypotenouse is", c)

print_right_triangle_dimensions()



'''
Q2. What does the following code print when uncommented?
Rewrite this code so that it is contained in a function
and both the code and the output makes it more clear
what the program is doing.
Test your function by calling it from the shell
'''
print(3.14 * 3.4 ** 2, ',', 2 * 3.14 * 3.4)

PI = 3.14
radius = 3.4
def print_numbers():
    circle_area = PI * radius ** 2
    circle_circumferance = 2 * PI * radius
    print(circle_area ,',', circle_circumferance)

print_numbers()



'''
Q3. Design a function that prints the area of
a 5.7 acre plot of land in square metres
Assume that 1 acre is 4046.85642 square metres
'''

def print_area():
    g = 5.7
    h = 4046.85642
    print("The area of a", g ,"acre plot of land in meters is", g * h ,"m")

print_area()

