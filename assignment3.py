FIRST_PURCHASE = 10
FREQUENT_BUYER = 2
NO_DISCOUNT = 0

def get_biggest(number1: int, number2: int, number3: int) -> int:
    '''
    takes 3 floating numbers and prints the largest one
    >>> get_biggest(756, 2345, 34523)
    34523
    >>> get_biggest(1, 2, 3)
    3
    >>> get_biggest(1123, 2342, 43)
    2342
    >>> get_biggest(2341, 652, 4563)
    4563
    '''
    if number1 > number2:
        if number1 > number3:
            return number1
        else:
            return number3
    elif number2 > number1:
        if number2 > number3:
            return number2
        else:
            return number3
    else:
        return number3
    

def get_smallest(number1: int, number2: int, number3: int) -> int:
    '''
    takes 3 floating numbers and prints the largest one
    >>>get_biggest(756, 2345, 34523)
    756
    >>> get_smallest(1, 2, 3)
    1
    >>> get_smallest(1123, 2342, 43)
    43
    >>> get_smallest(2341, 652, 4563)
    652
    >>> get_smallest(2,2,3)
    2
    
    '''
    if number1 < number2 and number1 < number3:
        return number1
    elif number2 < number1 and number2 < number3:
        return number2
    elif number1 == number2 and number1 < number3:
            return number1
    elif number1 == number2 and number1 > number3:
            return number3
    elif number1 == number3 and number1 < number2:
            return number1
    elif number1 == number3 and number1 > number2:
            return number2
    elif number2 == number3 and number2 < number1:
            return number2
    elif number2 == number3 and number2 > number1:
            return number1
    else:
        return (number3)
        

def is_multiple_of(n1: int, n2: int) -> bool:
    '''
    takes two integers n1 and n2 and determines whether 
    the first argument (n1) is a multiple of the second argument (n2)
    >>> is_multiple_of(8, 2)
    True
    >>> is_multiple_of(9, 2)
    False
    >>> is_multiple_of(0,4)
    True
    >>> is_multiple_of(4,0)
    False
    '''
    if n1 == 0:
        return True
    elif n2 == 0:
        return False
    elif n1 % n2 == 0:
        return True
    else:
        return False
    
    
def is_biggest_multiple_of_smallest(number1: int, number2: int, number3: int) -> bool:
    '''
    takes as arguments three integer values. The function should 
    determine whether the biggest of the three values is a multiple of the 
    smallest of the three values
    >>> is_biggest_multiple_of_smallest(8,3,2)
    True
    >>> is_biggest_multiple_of_smallest(9,3,5)
    True
    >>> is_biggest_multiple_of_smallest(23,4,7)
    False
    >>> is_biggest_multiple_of_smallest(346,0,57)
    False
    '''
    value = is_multiple_of(get_biggest(number1, number2, number3), get_smallest(number1, number2, number3))
    return value







def get_discount(discount: str, member: bool):
    '''
    gets discount and member from use and returns discount numebr
    >>> get_discount(FIRST_PURCHASE, False)
    10
    >>> get_discount(FREQUENT_BUYER, TRUE)
    2
    >>> get_discount(FREQUENT_BUYER, FALSE)
    0
    >>> get_discount(NO_DISCOUNT, True)
    0
    '''
    if discount == 'FIRST_PURCHASE':
        return FIRST_PURCHASE
    elif discount == 'FREQUENT_BUYER' and member == True:
        return FREQUENT_BUYER
    else:
        return NO_DISCOUNT
        

def get_discounted_price(discount: str, price: float, member: bool) -> float:
    '''
    returns a price after discount is applied
    >>> get_discounted_price(FIRST_PURCHASE, 12.00, True)
    2.0
    >>> get_discounted_price(FREQUENT_BUYER, 10.00, True)
    8.0
    >>> get_discounted_price(FREQUENT_BUYER, 10.00 False)
    10.0
    >>> get_discounted_price(NO_DISCOUNT, 10.00, False)
    10.0
    '''
    price -= get_discount(discount, member)
    if price <= 0:
        price = 0
    else:
        price += 0
    return price


def get_shipping(member: bool, country: str, price: float) -> float:
    '''
    returns shipping of item
    >>> get_shipping(True, 'Mexico', 10.00)
    0
    >>> get_shipping(False, 'Canada', 10.00)
    0
    >>> get_shipping(False, 'Germany', 10.0)
    1.0
    '''
    if country == 'Canada' or member == True:
        shipping = 0
        return shipping
    else:
        shipping = price * 0.1
        return shipping





def display_charges(price: float, tax: float, member: bool, discount: str, country: str) -> None:
    '''
    calculates the final bill for an online shopping site. The function should take the 
    following arguments where numeric values are assumed to be non-negative:

    the purchase price (ie. $ 15.99)
    the tax rate (ie. 8 % tax rate)
    a boolean value representing site membership - True if buyer is a member, False otherwise
    a discount code that should be one of: FIRST_PURCHASE, FREQUENT_BUYER, NO_DISCOUNT. 
    Any other values would not be valid discount codes.
    the country being shipped to (ie. Canada)
    
    >>> display_charges(22.0, 8, False, 'FIRST_PURCHASE', 'Mexico')
    price: $ 12.00
    tax: $ 0.96
    shipping: $ 2.20
    total charge: $ 15.16
    >>> display_charges(34.33, 5, True, none, Iraq)
    price: $ 34.33
    tax: $ 1.72
    shipping: $ 0.00
    total charge: $ 36.05
    '''
    
    
    shipping = get_shipping(member, country, price)
        
    price = get_discounted_price(discount, price, member)
    
    
        
        
    tax = price * (tax / 100)
    
    total_charge = price + tax + shipping
    
    print(f'price: $ {price:1.2f}')
    print(f'tax: $ {tax:1.2f}')
    print(f'shipping: $ {shipping:1.2f}')
    print(f'total charge: $ {total_charge:1.2f}')
    
