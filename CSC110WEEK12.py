#exception handling
x = '0'

try:
    # obviously this shouldnt work. but with try, it will go over 
    # the case and do what it says in except
    y = 10/int(x)
    print('y is:', y)
except ValueError:
    print('bad value for x')
    # value error output ex. x = 'ab'
    # bad value for x
    # the next part of the program continues...
except ZeroDivisionError:
    print('x was 0 - cannot divide by 0')
    # zero division error ex. x = '0'
    # x was 0 - cannot divide by 0
    # the next part of the program continues...
print('the next part of the program continues...')