#imutible type example and definition sort of. x is imutible btw
def foo(): 
    x = 5
    print(x) #first python gets and sees only x is 5, so it prints 5
    
    x = x + 10 
    print(x) #now python sees x has added 10 to its origional 5, so it prints 15
    
    bar(x) #now when we call bar, x is still 15, but now in bar, it adds 1, so it prints 16, when bar is called
    print(x) #now since bar is it's own thing, x is still 15 in foo, so it prints 15
    
def bar(x:int):
    x += 1
    print(x)
    
foo()


#return value example
#return value is weird asf
def doo():
    y = 5
    print(y) #first python gets and sees only y is 5, so it prints 5
    
    from_moo = moo(y) #now from_moo sees the function moo() and exicutes it so now y is 6
    print('doo\'s y:', y) #however, since we used return, it changes y back to 5 and displayes y
    print('from moo:', from_moo) #but from_moo y is 6, so it prints 6
    
def moo(y:int):
    y += 1
    print(y)
    return y
    
doo()



#return essentially keeps the data in a function and prints it, while print prints the value, but does not hold the data
def add1(n: int) -> int:
    
    n = n + 1
    return n  #works with return
    #print(n) #breaks with print

print('calling add1')
new_value = add1(40)
print('new_value:', new_value)
result = new_value * 2
print(result)



#return example
Begginer_start = 0
intermediate_start = 333
advanved_start = 667


def get_competency(comp: int) -> str: #-> variable is the type of variable you want to return
    if comp < intermediate_start:
        return 'beginner'
    elif comp < advanved_start:
        return 'intermediate'
    else:
        return 'advanced'
    
        
        
