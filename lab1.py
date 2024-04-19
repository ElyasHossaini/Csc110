def print_my_info():
    
    '''
    prints my name, favourite number, age, and math
    >>>My name is Elyas
    My favourite number is 36
    I am 18 years old
    Here is some math: 36 / 18 is 2.0
    '''
    favourite_number = 36
    my_age = 18
    
    print('My name is Elyas')
    print('My favourite number is', favourite_number)
    print('I am', my_age , 'years old')
    print('Here is some math:', favourite_number ,'/', my_age ,'is', favourite_number/my_age)
    
#calls function
print_my_info()



#initializes first_number and second_number to 23.2 and 82.4 as constants
first_number = 23.2
second_number = 82.4

def print_sum():
    '''
    adds the number 23.2 and 82.4
    >>>105.60000000000001
    '''
    print(first_number + second_number)
    
#calls function
print_sum()