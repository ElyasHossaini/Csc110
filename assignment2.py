def check_funds(credit_balance: float, dollar_purchase: float):
    '''
    takes two floating point numbers: the balance a person has on their credit card
    the dollar amount of the purchase they would like to make
    (function assumes this value is not negative) and prints your balance after the purchase
    >>>check_funds(34.22, 12.99)
    you will have $ 21.23 left after this purchase
    >>>check_funds(12.34, 14.11)
    you are short $ 1.77
    >>>check_funds(-34.22, 12.99)
    you have a negative balance
    '''
    
    if credit_balance >= dollar_purchase:
        credit_balance -= dollar_purchase
        print(f'you will have $ {credit_balance:1.2f} left after this purchase')
    elif credit_balance < 0:
        print('you have a negative balance')
    else:
        credit_balance = (credit_balance - dollar_purchase) * -1
        print(f'you are short $ {credit_balance:1.2f}')
        
        
        

def print_biggest(number1: float, number2: float, number3: float):
    '''
    takes 3 floating numbers and prints the largest one
    >>>print_biggest(756, 2345, 34523)
    34523.0
    >>>print_biggest(1, 2, 3)
    3.0
    >>>print_biggest(1123, 2342, 43)
    2342.0
    >>>print_biggest(2341, 652, 4563)
    4563.0
    '''
    if number1 > number2:
        if number1 > number3:
            print(number1)
        else:
            print(number3)
    elif number2 > number1:
        if number2 > number3:
            print(number2)
        else:
            print(number3)
    else:
        print(number3)
        
        


def convert_inches(total_inches: int):
    '''
    takes a number in inches from the user and displays the following number
    converted into miles, yards, feet, and inches
    >>>convert_inches(253536)
    4 mi, 2 yd, 2 ft, 0 in
    >>>convert_inches(63409)
    1 mi, 1 yd, 1 ft, 1 in
    '''
    miles = total_inches // 63360
    yards = (total_inches - (miles * 63360)) // 36
    feet = (total_inches - (miles * 63360) - (yards * 36)) // 12
    inches = (total_inches - (miles * 63360) - (yards * 36) - (feet * 12)) // 1
    
    print(miles ,'mi,', yards ,'yd,', feet ,'ft,', inches ,'in')
    



def is_multiple_of(n1: int, n2: int):
    '''
    takes two integers n1 and n2 and determines whether 
    the first argument (n1) is a multiple of the second argument (n2)
    >>>is_multiple_of(8, 2)
    8 is a multiple of 2
    >>>is_multiple_of(9, 2)
    9 is not a multiple of 2
    '''
    if n1 == 0:
        print(n1, 'is a multiple of', n2)
    elif n2 == 0:
        print(n1, 'is not a multiple of', n2)
    elif n1 % n2:
        print(n1 ,'is not a multiple of', n2)
    
    else:
        print(n1 ,'is a multiple of', n2)
        
        
#***
FIRST_PURCHASE = 10
FREQUENT_BUYER = 2
NO_DISCOUNT = 0
def display_charges(price: float, tax: float, member: bool, discount: str, country: str):
    '''
    calculates the final bill for an online shopping site. The function should take the 
    following arguments where numeric values are assumed to be non-negative:

    the purchase price (ie. $ 15.99)
    the tax rate (ie. 8 % tax rate)
    a boolean value representing site membership - True if buyer is a member, False otherwise
    a discount code that should be one of: FIRST_PURCHASE, FREQUENT_BUYER, NO_DISCOUNT. 
    Any other values would not be valid discount codes.
    the country being shipped to (ie. Canada)
    
    >>>display_charges(22.0, 8, False, 'FIRST_PURCHASE', 'Mexico')
    price: $ 12.00
    tax: $ 0.96
    shipping: $ 2.20
    total charge: $ 15.16
    >>>display_charges(34.33, 5, True, none, Iraq)
    price: $ 34.33
    tax: $ 1.72
    shipping: $ 0.00
    total charge: $ 36.05
    '''
    
    if country == 'Canada' or member == True:
        shipping = 0
        
    else:
        shipping = price * 0.1
        
        
    
    if discount == 'FIRST_PURCHASE':
        price -= FIRST_PURCHASE
    elif discount == 'FREQUENT_BUYER' and member == True:
        price -= FREQUENT_BUYER
    else:
        price -= NO_DISCOUNT
        
    if price <= 0:
        price = 0
    else:
        price += 0
        
    tax = price * (tax / 100)
    
    total_charge = price + tax + shipping
    
    print(f'price: $ {price:1.2f}')
    print(f'tax: $ {tax:1.2f}')
    print(f'shipping: $ {shipping:1.2f}')
    print(f'total charge: $ {total_charge:1.2f}')


    
    
    
    

    



        