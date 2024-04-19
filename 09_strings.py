import doctest
import math
'''
Q0.These functions appear to have similar behaviours but are very different.
'''

# Q0a. What is the difference between the expected output in the
# tests for these 2 functions?
#one prints while one returns

def string_return() -> str:
    """ demonstrate returning a string
    >>> string_return()
    'error'
    """
    value = 'error'
    return value


def string_print() -> None:
    """ demonstrate printing a string
    >>> string_print()
    error
    """
    value = 'error'
    print(value)

# The differences become much more clear when you call them....

# Q0b. if I execute the following code what is printed:
'''
error
'''
returned_value = string_return()
print(returned_value)

# Q0c. given your answer above, can I do this:
'''
yes
'''
sliced_str = returned_value[0:4]
print(sliced_str)


# Q0d. if I execute the following code what is printed:
returned_value = string_print()
print(returned_value)
'''
it will print error from string_print(), but returned_value has nothing in it
'''
# Q0e. given your answer above, can I do this:
'''
no
'''
#sliced_str = returned_value[0:4]
#print(sliced_str)


'''
Q1. Design a function that will take a word and determine whether
it is plural or not (ends with the letter s)
Assume any word that ends with s is plural (ie. pass is considered plural)
'''
def plural(word: str) -> None:
    if word[-1] == 's':
        print('is a plural')
    else:
        print('not a plural')

'''
Q2. Design a function that pluralizes a word if it is not already plural
The function should return a pluralized word (s added to the end).
We are going to assume anything with an s at the end is already pluralized.
'''
def pluralizer(word: str) -> None:
    if word[-1] == 's':
        print('is already a plural')
    else:
        print(f'{word}s')

'''
Q3. Design a function that takes a string and determines whether it
is composed of exactly 2 repeating strings ie. 'abcabc' is a repeating string.
'''
def repeat():
    word = input('word: ')
    repeatable = int(len(word) / 2)
    if word[:repeatable:] == word[repeatable::]:
        print('repeating string')
    else:
        print('not repeating')
repeat()

'''
Q4. Design a function that takes the amount of time an
object takes to fall after being dropped in seconds.
The function calculates and returns the distance the object fell in meters,
where the formula for distance is:
        d = 1/2 gt^2
        where t is the time in seconds and
        g is gravitational acceleration constant at 9.8 m/s^2
        d is in meters
If the function is passed a negative value for time it should
return the value -1 to indicate an error.
'''
g = 9.81
def dropped(time: float) -> float:
    if time < 0:
        return -1
    else:
        d = (1/2) * g * (time ** 2)
        return d
'''
Q5. Design another function that takes the distance in meters from a point
to the ground and a time in seconds.  The function should determine whether
the object will hit the ground in the given time.
The function should assume that both time and distance are not negative.
Make use of the previous function!
'''
def fall(distance: float, time: float) -> None:
    distance_with_time = dropped(time)
    if distance > distance_with_time:
        print('not possible')
    else:
        print('possible')
        
    

