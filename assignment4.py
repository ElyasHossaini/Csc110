def get_factors(n: int) -> int:
    '''
    takes an integer n and returns a string containing
    all of the factors of n from smallest to biggest separated by commas (,).
    >>> get_factors(0)
    0
    >>> get_factors(1)
    1
    >>> get_factors(12)
    1,2,3,4,12
    >>> get_factors(6)
    1,2,3,6
    '''
    result = ''
    if n == 0:
        return '0'
    elif n == 1:
        return '1'
    
    
    for i in range(1, n+1):
        if n % i == 0:
            result += str(i) + ','
    return result[:-1]




def get_range_of_factors(start: int, end: int) -> str:
    '''
    takes two integers: the first representing a starting point 
    and the second representing an end point. The function should 
    return a string containing rows with the factors all numbers from the given 
    start point (inclusive) to the given end point (not inclusive).
    All of the factors of a given number from smallest to biggest should be 
    separated by commas (,). Each set of factors should end with a newline.
    >>> get_range_of_factors(10,13)
    1,2,5,10
    1,11
    1,2,3,4,6,12
    >>> get_range_of_factors(0,3)
    0
    1
    1,2
    >>> get_range_of_factors(1,6)
    1
    1,2
    1,3
    1,2,4
    1,5
    '''
    result = ''
    for i in range(start, end):
        result += str(get_factors(i)) + '\n'
    return result





def sum_fibonacci_sequence(n: int) -> int:
    '''
    takes an integer n a returns the sum of the first n values in the Fibonacci sequence. 
    The function should assume the integer passed as an argument is not negative.
    >>> sum_fibonacci_sequence(0)
    0
    >>> sum_fibonacci_sequence(7)
    20
    >>> sum_fibonacci_sequence(1)
    0
    >>> sum_fibonacci_sequence(4)
    4
    '''
    current = 1
    previous = 0
    total = 1

        
    for i in range(2,n):
            nextnum = current + previous
            previous = current
            current = nextnum
            total += nextnum
    if n == 0:
        return 0
    elif n == 1:
        return 0
    else:
        return total









def print_tail(size: int) -> None:
    '''
    takes one argument representing the size of the rocket and prints the rockets 
    tail according to the give size.
    '''
    size = ('//  ') + ('/\  ' * size) + ('\\\\')
    print(size)



    
def print_booster(size: int) -> None:
    '''
    takes one argument representing the size of the rocket and prints the rockets
    booster according to the given size
    '''
    botton_size = size * 2 + 2
    #upper half
    for i in range(size+1):
        end_dots = size - i
        middles_dots = size * 2 - (i * 2)
        slashes = i + 1
        print('|' + ('.' * end_dots) + ('/\\' * slashes) + ('.' * middles_dots) + ('/\\' * slashes) + ('.' * end_dots) + '|')
    #lower half
    for i in range(size, -1, -1):
        end_dots = size - i
        middles_dots = size * 2 - (i * 2)
        slashes = i + 1
        print('|' + ('.' * end_dots) + ('\\/' * slashes) + ('.' * middles_dots) + ('\\/' * slashes) + ('.' * end_dots) + '|')
        
    print('+' + ('=*' * botton_size) + '+')




        
def print_instrument_unit(size: int) -> None:
    '''
    takes one argument representing the size of the rocket and prints the rockets
    instrument unit according to the given size
    '''
    unit_size = size * 2 + 1
    botton_size = size * 2 + 2
    print('||' + ('~#' * unit_size) + '||')
    print('||' + ('~#' * unit_size) + '||')
    print('+' + ('=*' * botton_size) + '+')





def print_lem_adapter(size: int) -> None:
    '''
    takes one argument representing the size of the rocket and prints the rockets
    lem adapter according to the given size
    '''
    number_of_percent_top = size * 2
    number_of_percent_bottom = size * 2 + 1
    botton_size = size * 2 + 2
    print(' //' + (' %' * number_of_percent_top) + '\\\\')
    print('//' + (' %' * number_of_percent_bottom) + '\\\\')
    print('+' + ('=*' * botton_size) + '+')
    




def print_space_craft(size: int) -> None:
    '''
    takes one argument representing the size of the rocket and prints the rockets
    space craft according to the given size
    '''
    botton_size = size * 2
    
    
    if size == 0:
        print('  ++')
    else:
        for i in range(1, size*2+1):
                slashes = i - 1
                spaces = size*2+3 - i
                print((' ' * spaces) + ('/' * slashes) + '**' + ('\\' * slashes))
        print('  +' + ('=*' * botton_size) + '+')



def print_rocket_ship(size: int, boosters: int) -> None:
    '''
    takes two arguments in the following order: one integer representing the size 
    of the rocket ship and one integer representing the number of boosters to be printed
    and prints a rocket according to those given numbers.
    '''
    print_space_craft(size)
    print_lem_adapter(size)
    print_instrument_unit(size)
    for i in range(boosters):
        print_booster(size)
    print_tail(size)
