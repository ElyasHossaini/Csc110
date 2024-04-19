import doctest

'''
Q1. Design a function called num_chars_before_vowel that takes a string
and counts and returns the number of characters in that string up to the
first vowel encountered.
NOTE: we are calling the following vowels - a,e,i,o,u

Use a while loop in your solution!
'''
def num_chars_before_vowel(word: str) -> int:
    
    count = 0
    vowel  = False
    
    while count < len(word) and vowel == False:
        if word[count: count + 1] == 'a' or word[count: count + 1] == 'e' or word[count: count + 1] == 'i' or word[count: count + 1] == 'o' or word[count: count + 1] == 'u':
            vowel = True
        else:
            count += 1
    
    print(count)



'''
Q2. Design a function that takes an integer and determines whether
it is prime or not.
NOTE: a number is prime if it is a positive number
divisible by 2 unique numbers, 1 and itself.
1 is not considered a prime number.
'''

def prime(number: int) -> bool:
    count = 0
    prime = True
    for i in range(1, number + 1):
        if number % i == 0:
            count += 1
    if count > 2:
        prime = False
    else:
        prime = True
    print(prime)

'''
Q3. Design a function that takes an integer n and prints the first n prime
numbers that exist with a comma between each.
Your function can assume n is not negative.
'''
def print_prime(number: int) -> None:
    result = ''
    for i in range(1, number+1):
        if number % i == 0:
            result += str(i) + ','
    print(result[:-1])



'''
Q4. Design a function that will take a number representing the size
and prints a pattern of slashes as demonstrated in the examples below
relative to the given size.
You can assume that size is greater than 0
Examples:
if size is 1, prints:
/
if size is 3, prints:
///
//\
/\\
if size is 4, prints:
////
///\
//\\
/\\\
'''
def slashes(size: int) -> None:
    for i in range(size):
        forward = size - i
        back = i
        print(('/' * forward) + ('\\' * back))
            

'''
Q5. Design a function that takes a non-negative number and
produces the given pattern as output:

if given 3 the following is printed:
123
234
345

if given 5 the following is printed:
12345
23456
34567
45678
56789
'''
def num(number: int) -> None:
    for i in range(1, number+1):
        for j in range(i, i + number):
            print(j, end='')
        print()
num(5)