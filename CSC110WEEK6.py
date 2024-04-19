# yoou can use the .lower() ethod to make things all lower case
#ex.
string = 'MONKEY'
lowercase = string.lower()
print(string) #MONKEY
print(lowercase) #monkey

#you can use the .isdigit() to cheeck wheather something has digits in it
#str float and negative number will be false
#ex.
var = 'lollypop'
var2 = 'lolly9090'
var3 = '34837843'
print(var.isdigit()) #False
print(var2.isdigit()) #False
print(var3.isdigit()) #True





#while loops
#basically while (something is true or false): do this.......
#you cant use float numbers in while loops, only int and negative ints
n = 1 
while n < 100:
    print(n)
    n *= 2
    
    


prompt = 'type yes message, anything else to stop '

#repeat = input(prompt)
keep_cheering = True

while keep_cheering:
    print('Go TEAM!')
    repeat = input(prompt)
    if repeat != 'yes':
        keep_cheering = False
    
    #repeat = input(prompt)
    
    
prompt2 = 'enter an int, -1 to stop'

val = int(input(prompt2))
while val != -1:
    print(val)
    val = int(input(prompt2))



# practice problems

def bar() -> int:
    s = 0
    num = int(input('enter a number: '))
    while num != -6:
        if num % 2 == 0:
            s += 1
        num = int(input('enter again: '))
    print(s)
bar()



def foo(count: int) -> None:
    total = 0
    while count > 0 and total < 8:
        total += count
        count -= 1
    print('count:', count, 'sum:', total)
foo(7)
#output: count: 5 sum: 13




#intro to list
my_int = 10

ages = [25, 29, 45, 104]

intrest_rates = [1.2, 3.4, 7.9]

names = ['bob', 'jojo', 'tian']

mixed = [1, 1.2, 'hello']

ages[0]


def length(values: list[int]) -> None:
    count = len(values)
    print(count)
    

for name in names:
    print(name)
    
nums = [1,2,5,6]
x = max(nums)
print(x)
'''
output is 6 because max number in nums is 6
'''
y = min(nums)
print(y)
'''
output is 1 because min number in nums is 1
'''
zoo = ['cat', 'dog', 'monkey']
biggestword = max(zoo)
print(biggestword)
'''
output is monkey because it is the largest word i.e. max word
'''

sumofnumber = sum(nums)
print(sumofnumber)
'''
outputs sum of numbers in nums
'''

#append adds another thing to the list
zoo.append('zebra')
#append will change the list