spacer_line = '/~~~~~~~~\\'
def print_logo():
    '''Prints two copies of each figure, alternating figures 
    (dog, monkey, dog, monkey) and prints the following spacer 
    line with no leading space: /~~~~~~~~\ before the first figure, 
    between figures and after the last figure.
    '''
    print(spacer_line)
    ascii_dog()
    print(spacer_line)
    ascii_monkey()
    print(spacer_line)
    ascii_dog()
    print(spacer_line)
    ascii_monkey()
    print(spacer_line)
    
    
def ascii_dog():
    '''
    prints dog ascii
    >>> ascii_dog()
          __      _
        o'')}____//
         `_/      )"
         (_(_/-(_/
    '''
    print('  __      _')
    print('o\'\')}____//')
    print(' `_/      )\"')
    print(' (_(_/-(_/')
    
ascii_dog()

def ascii_monkey():
    '''
    prints monkey ascii
    >>> ascii_monkey()
          /~\
         C oo"
         _( ^)
        /   ~\
    '''
    print('  /~\\')
    print(' C oo\"')
    print(' _( ^)')
    print('/   ~\\')

ascii_monkey()


PI = 3.14
def calculate_surface_area(cylinder_height: float, cylinder_diameter: float):
    '''
    calculates the surface area of a cylinder when given 
    a height and diameter and prints it out
    >>> calculate_surface_area(2, 4)
    cylinder area: 50.2
    >>> calculate_surface_area(1.2, 3.6)
    cylinder area: 32.4
    '''
    radius = cylinder_diameter / 2
    base_area = PI * radius ** 2
    rectangular_area = 2 * PI * radius * cylinder_height
    total_area = (2 * base_area) + rectangular_area
    print(f'cylinder area: {total_area:1.1f}')