# represent the following person information as a tuple person(NAME, AGE):
# the name
# the age
Person = tuple[str, float]
NAME = 0
AGE = 1

def file_to_person_list(file_name: str) -> list[Person]:
    '''
    take the name of a valid existing file as an argument and 
    will read the lines of text from a file that contains, on 
    each line: the name of a person and their age as a whole number separated by a space.
    >>> filename = 'lab8-name-age.txt'
    >>> file_to_person_list(filename)
    [('Lynden', 6), ('Tian', 27), ('Daljit', 18), ('Jose', 53), ('Jingwen', 17), ('Rajan', 65)]
    >>> file_to_person_list('emptyfile.txt')
    []
    '''
    new_list = []
    final_list = []
    file_handle = open(f'{file_name}', 'r')
    line = file_handle.readline()
    while line != '':
        info = line.split(' ')
        new_list.append(info[NAME])
        new_list.append(int(info[AGE]))
        list_to_tuple = tuple(new_list)
        final_list.append(list_to_tuple)
        new_list = []
        line = file_handle.readline()
    
    file_handle.close()
    return (final_list)


def get_average_age(person_info: list[Person]) -> float:
    '''
    takes a list with person information tuples and calculates and returns the average
    age of all ages in the list as a whole number (rounded down).
    >>> get_average_age([('Abe', 10), ('Tian', 45), ('Jose', 82)])
    45
    >>> get_average_age([('Abe', 10)])
    10
    >>> get_average_age([], 12)
    0
    '''
    num_elemets = len(person_info)
    age_total = 0
    for index in range(num_elemets):
        age_total += person_info[index][AGE]
    if num_elemets == 0:
        average_age = 0
    else:
        average_age = (age_total // num_elemets)
    return average_age

def get_above_age(person_info: list[Person], threshold_age: int) -> list[Person]:
    '''
    takes a list with person information tuples and a threshold age. The function should 
    create and return a list of all the person information tuples that have an age older 
    than the threshold age.
    >>> get_above_age([], 9)
    []
    >>> get_above_age([('Abe', 10), ('Tian', 45), ('Jose', 82)], 9)
    [('Abe', 10), ('Tian', 45), ('Jose', 82)]
    >>> get_above_age([('Abe', 10), ('Tian', 45), ('Jose', 82)], 83)
    []
    '''
    new_list = []
    num_elements = len(person_info)
    for index in range(num_elements):
        if person_info[index][AGE] > threshold_age:
            new_list.append(person_info[index])
    return new_list

def to_file(person_info: list[Person], file_name: str) -> None:
    '''
    takes a list with person information tuples and the name of a file as arguments and 
    writes the name and age from each tuple on its own line with the name and age separated 
    by commas.
    >>> to_file([], 'blankoutput.txt')
    
    >>> to_file([('Lynden', 6), ('Tian', 27), ('Daljit', 18), ('Jose', 53), ('Jingwen', 17), ('Rajan', 65)], 'output.txt')
    
    '''
    result = ''
    num_elements = len(person_info)
    file_handle = open(f'{file_name}', 'w')
    for index in range(num_elements):
        result += person_info[index][NAME] + ',' + str(person_info[index][AGE]) + '\n'
    file_handle.write(result)
    file_handle.close()
    

def write_names_above_avg_age(file_name_input: str, file_name_output: str) -> None:
    '''
    takes the name of an input file and the name of an output file. The input file 
    contains on each line a the name of a person and their age as a whole number 
    separated by a space. Your function can assume the file is perfectly formatted.
    The function should read all the names and ages from the input file and write 
    to the output file those names and ages above the average age of all ages of 
    people in the file.
    >>> write_names_above_avg_age('blank.txt', 'output.txt')
    
    >>> write_names_above_avg_age('filename.txt', 'output.txt')
    
    '''
    person_list = file_to_person_list(file_name_input)
    average_age = get_average_age(person_list)
    threshold_people = get_above_age(person_list, average_age)
    to_file(threshold_people, file_name_output)
    
    
        
    
        
    