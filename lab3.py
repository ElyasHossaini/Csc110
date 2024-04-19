def get_longer(number1: str, number2: str) -> str:
    '''
    user inputs 2 words and the longer word is then printed
    >>> get_longer(monkey, dog)
    monkey
    >>> get_longer(cat, log)
    cat
    >>> get_longer(log, monkey)
    monkey
    '''
    if len(number1) >= len(number2):
        return number1
    else:
        return number2
    
GST = 0.05
PST = 0.1
def get_tax(food: float, alcohol: float) -> float:
    '''
    user inputs amount of food, and amount of alcohol and returns
    the amount of tax owed 
    >>> get_tax(53.23, 23.42)
    8.836
    >>> get_tax(0, 23.23)
    3.4844999999999997
    >>> get_tax(34.32, 0)
    3.4320000000000004
    '''
    food_tax = food * GST
    alcohol_tax = (alcohol * PST) + (alcohol * GST)
    
    total = food_tax + alcohol_tax
    
    return total


def get_bill_share(food: float, alcohol: float, people: int) -> float:
    '''
    user inputs amount of food, and amount of alcohol  and number
    of people and returns the amount each owes
    >>> get_bill_share(53.23, 23.42, 2)
    42.743
    >>> get_tax(0, 23.23, 4)
    6.678625
    >>> get_tax(34.32, 0, 6)
    6.2920000001
    >>> get_tax(53.23, 23.42, 1)
    84.7678
    '''
    total = (food + alcohol + get_tax(food, alcohol)) / people
    return total
    
    

    





