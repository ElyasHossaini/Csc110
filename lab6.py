def sum_even_values(the_list: list[int]) -> int:
    '''
    takes a list of integers as an argument and calculates 
    and returns the sum of only the values in the list that are even.
    >>> sum_even_values([])
    0
    >>> sum_even_values([0,1,2,3,4])
    6
    >>> sum_even_values([1,3,5])
    0
    >>> sum_even_values([2,4,6])
    12
    '''
    sum1 = 0
    num_elements = len(the_list)
    for values in range(num_elements):
        if the_list[values] % 2 == 0:
            sum1 += the_list[values]
    return (sum1)


def count_above(numbers: list[int], threshold: int) -> int:
    '''
    takes a list of numbers and a threshold value as arguments and counts 
    and returns the number of values in the list that are above the given threshold.
    >>> count_above([1,2,3,4,5], 3)
    2
    >>> count_above([1,2,3,4], 0)
    4
    >>> count_above([0], 12)
    0
    '''
    num_elements = len(numbers)
    number_of_values = 0
    for values in range(num_elements):
        if numbers[values] > threshold:
            number_of_values += 1
    return (number_of_values)


def add1(numbers: list[int]) -> list[int]:
    '''
    takes a list of integers as an argument and creates and returns a new list
    with every value in the given list with 1 added to it
    >>> add1([1,2,3,4])
    [2, 3, 4, 5]
    >>> add1([0,0,0,0])
    [1, 1, 1, 1]
    >>> add1([2,1,3,3])
    [3, 2, 4, 4]
    >>> add1([])
    []
    '''
    final_list = []
    num_elements = len(numbers)
    for values in range(num_elements):
        final_list.append(numbers[values] + 1)
    
    return (final_list)


def are_all_even(numbers: list[int]) -> bool:
    '''
    takes a list of integers and determines whether all of the elements in the list are even.
    >>> are_all_even([3,4,5])
    False
    >>> are_all_even([])
    True
    >>> are_all_even([2,2,2])
    True
    '''
    count = 0
    num_elements = len(numbers)
    is_even = True
    
    for index in range(num_elements):
        if numbers[index] % 2 == 0:
            count += 1
        
    if count == num_elements:
        is_even = True
    else:
        is_even = False
    return (is_even)

    


