import doctest

# we designed this function in a past lecture:


def get_number() -> int:
    """ repeatedly prompts user for a number >=0
    and returns it as an int
    """
    prompt = 'enter a whole number >=0: '
    num_as_str = input(prompt)
    while not num_as_str.isdigit():
        num_as_str = input(prompt)

    return int(num_as_str)


'''
Q1. Design a function called print_list that takes a list of numbers and
prints all the numbers in the list separated by a comma and space and
enclosed in square brackets.

Use a loop to do this, don't just use print(list_of_numbers)
'''


'''
Q2. Design a function that will repeatedly prompt the user to enter
positive whole numbers and 0 to stop.
The function should create and return a list that holds all of the positive
integers entered by the user.
The function should ignore invalid input (ie. floats, words, negative values)
'''


'''
Q3. Design a function that takes a list of numbers and returns the sum
of the numbers in the list.
Do not use the builtin sum function.
'''


'''
Q4. Design a function that takes a list of integers and returns a new list
with the numbers from the given list with all odd numbers removed.

Example: if called as: keep_even([3, 61, 4, 3, 2, 5])
it should return the list [4, 2]
'''


'''
Q5. Design a function that takes a list of integers and
an additional integer value.
The function should return the index of the first occurrence of
the additional integer within the list.
If the value is not found in the list, the function should
return -1.
Do not use the builtin list index function
'''
