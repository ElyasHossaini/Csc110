def print_name_age_v1() -> None:
    '''
    prompts the user to enter their name and then prompts them to enter 
    their age. It then prints hello followed by the name and the category of the age.
    '''
    name = input('Enter your name: ')
    age = int(input('Enter your age: '))
    if age < 18:
        age_category = 'child'
    elif age >= 65:
        age_category = 'senior'
    else:
        age_category = 'adult'
    print('hello', name, age_category)


def print_name_age_v2() -> None:
    '''
    prompts the user to enter their name and then prompts them to enter their age. 
    It then prints hello followed by the name and the category of the age. 
    If the user enters an invalid age (ie, letters, a number smaller than 0, etc…) 
    it prints the name followed by you are lying about your age.
    '''
    name = input('Enter your name: ')
    age = input('please enter your age: ')
    if age.isdigit() == False:
        print(name, 'you are lying about your age')
    else:
        age = int(age)
        if age < 18:
            age_category = 'child'
        elif age >= 65:
            age_category = 'senior'
        else:
            age_category = 'adult'
        print('hello', name, age_category)


def get_num(min_val: int, prompt: str) -> int:
    '''
    takes two arguments: an integer that represents a minimum value and a string to use
    as a prompt for the user. The function should repeatedly ask the user with the given 
    prompt to enter a number until the user enters a valid integer greater than or equal
    to the given minimum. The function should return the valid entry as an integer.
    '''
    while True:
        response = input(prompt)
        
        
        if response.isdigit():
            num = int(response)
            if num >= min_val:
                return num
        



def print_name_age_v3() -> None:
    '''
    prompts the user to enter their name and then prompts them to enter a number 
    for their age. It then prints hello followed by the name and the category of 
    the age. If the user enters an invalid age (ie, letters, a number smaller than 0) 
    it will continue to ask the user for a number until they enter a number that is a 
    valid age.
    '''
    name = input('Enter your name: ')
    age = get_num(0, 'Please enter age: ') 
    if age < 18:
        age_category = 'child'
    elif age >= 65:
        age_category = 'senior'
    else:
        age_category = 'adult'
    print('hello', name, age_category)
