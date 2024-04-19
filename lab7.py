#represent the following flight information as a tuple 
#containing: the departure city, the arrival city and the duration of the flight.
#information(Departure, Arrival, Time)
#where Time > 0
#Make sure city names are not empty strings and have proper capitalization
Flight_Info = tuple[str, str, int]
DEPARTURE = 0
ARRIVAL = 1
TIME = 2

def swap(values: list, position1: int, position2: int) -> None:
    '''
    takes a list of values as an argument and two additional arguments that 
    represent positions in the list. The function should swap the values at
    specified positions in the list.
    '''
    position1_val = values[position1]
    position2_val = values[position2]
    values[position1] = position2_val
    values[position2] = position1_val

    
    
def index_of_smallest(values: list) -> int:
    '''
    takes a list of values as an argument and finds and returns the position of the smallest value.
    If there are duplicate entries of the smallest value, the function should return the index 
    of the first occurrence. If the list is empty, the function should return -1.
    >>> index_of_smallest([-21, -20, -5, -3, -14, 4, 7, -2, -7, 8, -11, -1, -16, -8, -9])
    0
    >>> index_of_smallest([-7, 2, -18, -14, -12, 1, -11, -4, 8, -15, -13, 17, 6, -8, 14, -21])
    15
    >>> index_of_smallest([])
    -1
    >>> index_of_smallest([1,2,3,1])
    0
    >>> index_of_smallest(['a', 'b', 'd', 'c', 'a'])
    0
    >>> index_of_smallest(['a', 'b', 'd', 'c', 'A'])
    4
    '''
    smallest = 999999
    position_smallest = 0
    if not values:
        position_smallest = -1
    else:
        for num in range(len(values)):
            if values[num] < smallest:
                smallest = values[num]
                position_smallest = num
        
    return (position_smallest)


def total_duration(information: list[Flight_Info]) -> int:
    '''
    takes a list of flight information tuples. The function should calculate and
    return the total duration of all flights in the given list.
    >>> total_duration([('Victoria', 'Mexico City', 5.5), ('Vancouver', 'Toronto', 4)])
    9.5
    >>> total_duration([])
    0
    >>> total_duration([('Victoria', 'Mexico City', 5.5)])
    5.5
    '''
    total_duration = 0
    num_elements = len(information)
    for index in range(num_elements):
        total_duration += information[index][TIME]
    return (total_duration)



def get_destinations_from(information: list[Flight_Info], departure_city: str) -> list[str]:
    '''
    takes a list of flight information tuples and a departure city. The function should 
    return a list of all the unique destinations that are flown to from the given departure city.
    >>> get_destinations_from([('Victoria', 'Vancouver', 0.75), ('Vancouver', 'Toronto', 4), ('Victoria', 'Calgary', 1.5), ('Victoria', 'Vancouver', 0.5)], 'Victoria')
    ['Vancouver', 'Calgary']
    >>> get_destinations_from([], 'Calgary')
    []
    >>> get_destinations_from([('Victoria', 'Vancouver', 0.75)], '')
    []
    '''
    new_list = []
    num_elements = len(information)
    for index in range(num_elements):
        if information[index][DEPARTURE] == departure_city:
            if information[index][ARRIVAL] not in new_list:
                new_list.append(information[index][ARRIVAL])
    return (new_list)

