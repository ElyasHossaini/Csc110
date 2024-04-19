#list tuples
nums = [1,2,3]
nums[0] = 10
# output:
#     [10,2,3] basically changes the one you chose

my_tuple = (2,3,6)
print(my_tuple)
#output:
#   (2,3,6)
#TUPLES CANNOT BE UPDATED AFTER CREATION
#TUPLES CANNOT BE UPDATED AFTER CREATION
#TUPLES CANNOT BE UPDATED AFTER CREATION
#TUPLES CANNOT BE UPDATED AFTER CREATION
#TUPLES CANNOT BE UPDATED AFTER CREATION


#can add tuples together
other_tuple = (3,5,8)
together_tuple = other_tuple + my_tuple

#can make tuple into list
new_list = list(together_tuple)

#to acess position 0 in a tuple, you need to add a (,) after the number
#Ex.
my_tuple2 = (3,)
my_tuple2[0]
#without calma wont work

vals = (1,2,3,4)
#quiz questions
def fn2(vals):
    values = []
    for index in range(len(vals)):
        values.append(vals[index] + 2)
    return tuple(values)

def fn3(vals):
    values = list(vals)
    for index in range(len(vals)):
        values[index] = values[index] +2
    return tuple(values)

fn3(vals)
print(vals)


Name = 0
age = 1


#represents a person(name, age)
#where age>=0
#this is custom type hint
PersonInfo = tuple[str, int]


#tuples are used to contain everything, not just a single variable type
def print_name(person: tuple[str, int]) -> None:
    print(person[Name], 'is:', person[age], 'years old.')
print_name(('elyas', 18))

def print_names(group: list[PersonInfo]) -> None:
    for person in group:
        print_name(person)
    



#nested loops with lists

def multiply_by_scalar(lovals: list[int], multiplier: int) -> list[int]:
    new_list = []
    for val in lovals:
        new_list.append(val * multiplier)
    return new_list

def multiply_by_list(list1: list[int], list2: list[int]) -> list[list[int]]:
    '''
    creates and returns a new list of lists, where each list added
    to the new list is list1 multiplied by an element in list2
    >>> multiply_by_list([], [])
    []
    >>> multiply_by_list([], [1,2])
    [[], []]
    >>> multiply_by_list([2,3], [])
    []
    >>> multiply_by_list([2,3], [4,5,6])
    [[8,12], [10,15], [12,18]]
    '''
    list_of_lists = []
    
    for num_list2 in list2:
        new_sublist = multiply_by_scalar(list1, num_list2)
        list_of_lists.append(new_sublist)
    
    return list_of_lists


#quiz questions

def foo(a, b):
    x = 0
    
    for num2 in b:
        for num1 in a:
            y = num1 + num2
            x += 1
            
    return x
result = foo([2,6,4], [1,8])
print(result)
#total looping is 6 because 3*2


def boo(a, b):
    x = 0
    
    for num2 in b:
        x += 1
        for num1 in a:
            y = num1 + num2
            
            
    return x
result = boo([6,3,2,5], [5,7,4])
print(result)
#total run is 3 because outer list is 3


def doo(a, b):
    x = []
    
    for num2 in b:
        for num1 in a:
            y = num1 + num2
            x.append(y)
            
    return x
result = doo([3,1], [5,7,2])
print(result)
#output based on 3+5, 1+5, 3+7, 1+7, 3+2, 1+2
#all the left added to one right at a time

def cn1(a, b):
    x = []
    for num2 in b:
        z = []
        for num1 in a:
            w = num1 + num2
            z.append(w)
        x.append(z)
    return x
result = cn1([6,3,5], [1,4])
print(result)
#output: is basically making 2 list first being all values in list1 added to 
# first value in list2 and the second list is all values in list 1 added to second 
# value in list 2
#[[6, 7, 9, 10], [10, 11, 13, 14]]


def cn2(a, b):
    x = []
    z = []
    for num2 in b:
        
        for num1 in a:
            w = num1 + num2
            z.append(w)
        x.append(z)
    return x
result = cn2([4,5,7,8], [2,6])
print(result)
#output: is basically double the list of all values in list1 add to values in list 2
#[[6, 7, 9, 10, 10, 11, 13, 14], [6, 7, 9, 10, 10, 11, 13, 14]]



def choo(a, b):
    x = []
    z = len(a)
    for y in range(z):
        t = a[y] + b[y]
        x.append(t)
    return x

result = choo([7,5], [3,1,4,8,2,6])
print(result)
#output is basically element 0 of each is added and now is element 0 of a new list
#[10, 6]
#will only output if left side has less elements than right side. otherwise there in an error