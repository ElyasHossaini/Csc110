#you can compare strings obviuosly.
#use (in) function to check if stuff is in string
#EX. 'put' in 'computer
#True
#when compairing 2 strings, only compares the value of the first letter. Capitols are worth less then undercase
#Ex.
'''
>>>'bRYAN > Bryan'
True
>>>'Bryan > bRYAN'
False
'''

#String slicing Example
#use [] to get value of string. goes from 0-x
phrase = 'hello my friend'
phrase[0]
'''
>>>phrase[0]
h
>>>phrase[15]
invalid
>>>phrase[14]
d
>>>phrase[-1]
d
>>>phrase[-15]
h
'''
#chose slice with [:] the dotty thing. if u go from 1:4, only shows 1, 2, 3. but not 4
#default start 0 if not value. i.e. phrase[:5]
# #if both empty, prints whole thing
phrase[1:4]
'''
>>>phrase[1:4]
ell
>>>phrase[0:15]
hello my friend
>>>phrase[:5]
hello
>>>phrase[:-1]
hello my frien
>>>phrase[-6:]
friend
'''

new_phrase = phrase[1:4]
#input: print(new_phrase)
#outpu: ell




#boolean return value
def is_even(num: int) -> bool:
    '''
    >>>is_even(16)
    True
    >>>is_even(21)
    False
    '''
    if num % 2 == 0:
        return True
    else:
        return False
#if expression is True, it returns True
#if expression is False, returns False
#so no need to if else statement

def is_even2(num: int) -> bool:
    return num % 2 == 0
#now this will return true or false depending oon the number
#only works for booleans
