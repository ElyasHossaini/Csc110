def compute_harmonic_series(n: int) -> float:
    '''
    takes an integer n and computes and returns 
    the sum of the harmonic series to n 
    >>> compute_harmonic_series(4)
    2.083333333333333
    >>> compute_harmonic_series(-3)
    0.0
    >>> compute_harmonic_series(1)
    1.0
    >>> compute_harmonic_series(2)
    1.5
    '''
    if n < 0:
        return 0
    
    series = 0
    for i in range(1, n+1):
        series += 1/i
    return series





def get_fibonacci_sequence(n: int) -> str:
    '''
    takes an integer n and returns a string 
    containing the first n values in the Fibonacci 
    sequence separated by commas.
    >>> get_fibonacci_sequence(-1)
    'None'
    >>> get_fibonacci_sequence(0)
    ''
    >>> get_fibonacci_sequence(1)
    '0'
    >>> get_fibonacci_sequence(2)
    '0,1'
    >>> get_fibonacci_sequence(5)
    '0,1,1,2,3'
    '''
    if n < 0:
        return 'None'
    
    result = '0,1,'
    if n == 0:
        return ''
    elif n == 1:
        return '0'
    elif n == 2:
        return '0,1'
    else:
        current = 1
        previous = 0
        for i in range(2,n):
            nextnum = current + previous
            previous = current
            current = nextnum
            result += str(nextnum) + ','
        return result[:-1]
            
            
            



def print_pattern(height: int, width: int, character1: str, character2: str) -> None:
    '''
    takes 2 integers representing the height 
    and width and 2 strings representing characters 
    to be printed and prints a pattern
    >>> print_pattern(4,3,'lol','mom')
    lolmomlolmomlolmomlolmom
    momlolmomlolmomlolmomlol
    lolmomlolmomlolmomlolmom
    >>> print_pattern(4,3,'munk','joe')
    monkjoemonkjoemonkjoe
    joemonkjoemonkjoemonk
    monkjoemonkjoemonkjoe
    joemonkjoemonkjoemonk
    >>> print_pattern(1,0,'link','up')
    
    >>> print_pattern(0,1,'link','up')
    
    >>> print_pattern(1,1,'link','up')
    linkup
    '''
    if height < 0 and width < 0:
        print('no height or width')
        
        
    for i in range(height):
        if i % 2 == 0:
            for j in range(width):
                print(character1,character2, sep='', end='')
            print()
        else:
            for j in range(width):
                print(character2,character1, sep='', end='')
            print()
