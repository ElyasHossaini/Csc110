meters = 4046.85642

def acres_to_sqr_meters():
    acres = 5.7

    sqr_meters = acres * meters
    print('Area is: ', sqr_meters, 'm^2')
    
acres_to_sqr_meters()


'''
Q1a. The function definition above is a solution to the problem I left you
with at the end of last lecture.
How can we make this function easier for some reading it to quickly
comprehend what the function does?
'''

    #put meters as a constant
    

'''
Q1b. The acres_to_sqr_meters function is not very versatile -
it will only calculate the square meters for 5.7 acres!
Edit the function so that it will calculate the square meters
for ANY non-negative number of acres.
'''

def acres_to_sqr_meter(acres: float):
    sqr_meters = acres * meters
    print('Area is ', sqr_meters, 'm^2')

'''
Q2. Design a function that will take the name of the best team and
print out a cheer for that team.
'''
    
    
def best_team(teamname: str):
    print('Go', teamname ,'Go!')
    
def best_team1():
    teamname1 = input('whats your favourite team?')
    print('Go', teamname1 ,'Go!')

best_team1()

'''
Q3. Design a function called print_bill that takes the
price of a clothing item. The function should print the bill
which should include the following items:
 the price, the PST amount, the GST amount, and the total bill including taxes
NOTE: PST is provincial sales tax at 7%
      GST is goods and services tax at 5%
'''

PST = 0.07
GST = 0.05

def print_bill():
    price = float(input("Enter price of cloths: "))
    PST_amount = price * PST
    GST_amount = price * GST
    total = price + PST_amount + GST_amount
    
    print('Clothing price:', price)
    print(f'PST amount: {PST_amount:1.2f}')
    print(f'GST amount: {GST_amount:1.2f}')
    print(f'Total bill including taxes: {total:1.2f}')
    

print_bill()


#or
def print_bill2(price: float):
    PST_amount = price * PST
    GST_amount = price * GST
    total = price + PST_amount + GST_amount
    
    print('Clothing price:', price)
    print(f'PST amount: {PST_amount:1.2f}')
    print(f'GST amount: {GST_amount:1.2f}')
    print(f'Total bill including taxes: {total:1.2f}')


    

    

'''
Q4. Design a function that will take a person's name and age and will
print a personalized message for that person.
For example, if we call the function as: welcome('Amy', 21)
the function should print:  Welcome Amy! Amy's 21 years old.
'''

def message():
    name = input('Enter your name:')
    age = input('Now enter your age:')
    
    print('Welcome', name ,'\nYou are', age ,'aren\'t you?')
    
    
    
message()


#or

def message_2(name: str, age: int):
    print('Welcome', name ,'\nYou are', age ,'aren\'t you?')
    
