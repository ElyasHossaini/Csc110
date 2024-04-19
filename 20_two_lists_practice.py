import doctest


'''
Q0. Complete the function below from last lecture.
'''

def zip_longer(list1: list[int], list2: list[int], fill_val: int
               ) -> list[tuple[int, int]]:
    """ creates and returns a list of tuples for pairs across list1 and list2,
    fills missing values with fill_val
    >>> zip_longer([], [], 2)
    []
    >>> zip_longer([2, 3, 4], [], 1000)
    [(2, 1000), (3, 1000), (4, 1000)]
    >>> zip_longer([], [5, 6, 7], 1)
    [(1, 5), (1, 6), (1, 7)]
    >>> zip_longer([8, 9, 10], [5, 6, 7], 1)
    [(8, 5), (9, 6), (10, 7)]
    >>> zip_longer([8, 9, 10], [5, 6], 2)
    [(8, 5), (9, 6), (10, 2)]
    >>> zip_longer([8, 9], [5, 6, 7], 2)
    [(8, 5), (9, 6), (2, 7)]
    """
    num_elements_list1 = len(list1)
    num_elements_list2 = len(list2)
    total_elements = 1
    appending_list = []
    final_list = []
    if num_elements_list1 > num_elements_list2:
        total_elements = num_elements_list1
    else:
        total_elements = num_elements_list2
    
    for index in range(total_elements):
        if total_elements > num_elements_list1:
            appending_list.append(fill_val)
            appending_list.append(list2[index])
            new_tuple = tuple(appending_list)
            final_list.append(new_tuple)
            appending_list = []
        elif total_elements > num_elements_list2:
            appending_list.append(list1[index])
            appending_list.append(fill_val)
            new_tuple = tuple(appending_list)
            final_list.append(new_tuple)
            appending_list = []
        else:
            appending_list.append(list1[index])
            appending_list.append(list2[index])
            new_tuple = tuple(appending_list)
            final_list.append(new_tuple)
            appending_list = []
    print(final_list)
           
zip_longer([], [], 2) 
zip_longer([2, 3, 4], [], 1000)
zip_longer([], [5, 6, 7], 1)
zip_longer([8, 9, 10], [5, 6, 7], 1)
zip_longer([8, 9, 10], [5, 6], 2)
zip_longer([8, 9], [5, 6, 7], 2)      

'''
Q1. Design a function that will take two lists of integers
that are in increasing order. The function should
create and return a list of all the values from list1 and list2
in sorted order
ie. if the function is called with [2, 10], [5, 6, 11]
the function should return [2, 5, 6, 10, 11]
'''
def two_list(list1: list[int], list2: list[int]) -> list[int]:
    lisr = list1 + list2
    lisr.sort()
    print(lisr)
two_list([2,10], [5,6,11])


'''
Q2. Design a function that will sort a given list of integers.
The function should use a selection sort algorithm:
for each position in the given list,
-finds the position of the smallest value between 
the current position and the end of the list
-swaps the values at the current position and
the position of the smallest value
NOTE: this function will mutate the list
TIP: use the functions you wrote in lab as helper functions
'''


'''
Q3. Design a function that takes 2 lists of integers and determines whether the
first list is strictly contained in the second list.
You should not need a nested loop to solve this problem.
For example,
[1, 4, 3] is contained in [1, 1, 4, 3]
[1, 4, 3] is not contained in [1, 1, 4, 4, 3]
'''
