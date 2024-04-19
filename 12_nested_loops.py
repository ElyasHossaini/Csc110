import doctest


'''
Q1. Design a function that takes a string and 2 numbers
representing height and width.
The function should print a rectangular pattern using the given string
that is of dimension width by height.
You can assume that height and width are not negative and the string is not empty
Example. if the string is '*#' and height is 4 and width is 3, it should print:
*#*#*#
*#*#*#
*#*#*#
*#*#*#
You must not use the * operator to repeat your string.
'''
def rectanglepattern(pattern: str, height: int, width: int) -> None:
  for i in range(height):
    for j in range(width):
      print(pattern, sep='', end="")
    print()

# a function from last lecture exercises...
def get_repeat(n:int, string:str) -> str:
    """ returns a string with given string repeated n times
    Precondition: n>=0
    >>> get_repeat(0,'ab')
    ''
    >>> get_repeat(5,'')
    ''
    >>> get_repeat(4,'ab cd')
    'ab cdab cdab cdab cd'
    """
    new_string = ''
    for count in range(n):
        new_string += string
    
    return new_string

'''
Q2. Design a function that will take a number representing height and it
should print a right angle triangle using '*'s that is of the given height.
You can assume that size is greater than or equal to 0
Examples:
if ht is 2, prints:
*
**
if ht is 3, prints:
*
**
***
'''
def triangle(height: int) -> None:
  for i in range(height+1):
      print('*' * i)
  print()

'''
Q3. Design a fucntion that takes a non-negative number that represents a size
and prints a number pattern according to the size.
You can assume that size is greater than or equal to 0
Examples:
if the size is 3 it prints...
3
32
321
if the size is 5 it prints...
5
54
543
5432
54321
'''
def countdown(size: int) -> None:
  for i in range(size, 0, -1):
    for j in range(size, i-1, -1):
      print(j, end='', sep='')
    print()

'''
Q4. Design a function that will take a number representing height and it
should print an isosceles triangle using '*'s that is of the given height.
You can assume that size is greater than or equal to 0
TIP: to get the stars to appear centered, think about how many space (' ')
characters to print on a row before you print the * characters.
Examples:
if ht is 2, prints:
 *
***
if ht is 3, prints:
  *
 ***
*****
'''

def iso(height: int) -> None:
    for i in range(height+1):
      spaces = height - i - 1
      stars = 2 * i + 1
      print(' ' * spaces + '*' * stars)
    print()
iso(5)
'''
Q5. Design a function that will take a number representing height and it
should print a diamond using '*'s that is of the given height.
You can assume that size is greater than or equal to 0
Examples:
if ht is 2, prints:
 *
***
 *
if ht is 3, prints:
  *
 ***
*****
 ***
  *
'''
def print_diamond(ht):
# Upper half (including the middle line)
    for i in range(ht):
        print(' ' * (ht - i - 1) + '*' * (2*i + 1))
    
    # Lower half
    for i in range(ht-2, -1, -1):
        print(' ' * (ht - i - 1) + '*' * (2*i + 1))