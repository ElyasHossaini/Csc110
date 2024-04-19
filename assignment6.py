def get_powers(numbers: list[int], power: int) -> list[int]:
    '''
     takes a list as an argument and an additional argument as a power. 
     The function should create and return a new list that contains every
     element in the given list raised to the given power.
     >>> get_powers([], 2)
     []
     >>> get_powers([0,1,2,3], 2)
     [0,1,4,9]
     >>> get_powers([1,2,3,4], 0)
     [1,1,1,1]
    '''
    new_list = []
    num_elements = len(numbers)
    for index in range(num_elements):
        new_list.append(numbers[index] ** power)
    return (new_list)
    




def concatenate(the_list: list[str]) -> str:
    '''
    takes a list of strings as an argument. The function 
    should return a single string containing all values from 
    the given list, in the order they appear in the list, separated
    by a single space character.
    >>> concatenate(['monkey', 'cow', 'hoarse'])
    'monkey cow hoarse'
    >>> concatenate(['potatoes', 'carrots', '', 'ferret', 'lunch'])
    'potatoes carrots  ferret lunch'
    >>> concatenate([])
    ''
    '''
    result = ''
    num_elements = len(the_list)
    for index in range(num_elements):
        result += the_list[index] + ' '
        
    return (result[:-1])




def contains_multiple(numbers: list[int], additional_num: int) -> bool:
    '''
    takes a list of integers as an argument and an additional integer argument.
    The function should determine whether there exists a value in the list that
    is a multiple of the given additional integer. 
    >>> contains_multiple([9, 17, 38, -493],29)
    True
    >>> contains_multiple([9, 21, 37, 7, 31, 10, 36, 15, 32, 20, 25, 14, 8, 28, 23],0)
    False
    >>> contains_multiple([], 2)
    False
    >>> contains_multiple([12, 38, 9, 6, 34, 7, 0, 29, 11, 39, 21, 20, 14],0)
    True
    >>> contains_multiple([4,5],3)
    False
    '''
    num_elements = len(numbers)
    count = 0
    is_multiples = False
    for index in range(num_elements):
        if numbers[index] != 0 and additional_num == 0:
            count += 0
        elif numbers[index] == 0 and additional_num == 0:
            count += 1
        elif abs(numbers[index]) % additional_num == 0:
            count += 1
        else:
            count += 0
        
    if count >= 1:
        is_multiples = True
    else:
        is_multiples = False
            
    
    return (is_multiples)





def get_long_enough(the_list: list[str], threshold: int) -> list[str]:
    '''
    takes a list of strings as an argument and an addtional integer as a 
    threshold. The function should return a list of all strings in the given 
    list that are at least as long as the given threshold.
    >>> get_long_enough([], 10)
    []
    >>> get_long_enough(['cow', 'pig' 'at'], 3)
    ['cow', 'pig']
    >>> get_long_enough(['cow', 'pig', 'at'], 2)
    ['cow', 'pig', 'at']
    >>> get_long_enough(['cow', 'pig', 'at'], -2)
    ['cow', 'pig', 'at']
    >>> get_long_enough(['cow', 'pig', 'at'], 4)
    []
    
    '''
    new_list = []
    num_elements = len(the_list)
    for index in range(num_elements):
        if len(the_list[index]) >= threshold:
            new_list.append(the_list[index])
    return (new_list)






def all_multiples(numbers: list[int], additional_num: int) -> bool:
    '''
    takes a list of integers as an argument and an additional integer argument. 
    The function should determine whether all values in the list are multiples of 
    the given additional integer. 
    >>> all_multiples([10, -18, 13, -7, 17, -19, -6, 18, -2, 15, -16, 9, -20], 0)
    False
    >>> all_multiples([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 0)
    True
    >>> all_multiples([], 3)
    False
    >>> all_multiples([2,4,6], 2)
    True
    >>> all_multiples([5,7,9], 2)
    False
    '''
    num_elements = len(numbers)
    count = 0
    is_multiples = False
    

    for index in range(num_elements):
            if numbers[index] != 0 and additional_num == 0:
                count += 0
            elif numbers[index] == 0 and additional_num == 0:
                count += 1
            elif abs(numbers[index]) % additional_num == 0:
                count += 1
            else:
                count += 0
    if count == num_elements:
            is_multiples = True
    else:
            is_multiples = False
    
    return (is_multiples)
    

       
       
       
       
       
            

def getting_shorter(words: list[str]) -> bool:
    '''
    takes a list of strings as an argument. The function determines 
    whether the strings are in order of strictly decreasing lengths.
    >>> getting_shorter([])
    False
    >>> getting_shorter(['potatoes'])
    False
    >>> getting_shorter(['nggqnulowlh', 'pfxvvtierv', 'ffoseneo', 'kiztuz', 'ab'])
    True
    >>> getting_shorter(['lol', 'cow', 'at'])
    False
    '''
    num_elements = len(words)
    count = 0
    is_shorter = True
    for index in range(num_elements):
        if index != 0:
            if len(words[index]) < len(words[index-1]):
                count += 1
        else:
            count += 1
                
    if count == num_elements:
        is_shorter = True
    else:
        is_shorter = False
    
    return (is_shorter)



