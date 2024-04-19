#Extra example of using def with lots of things
PI = 3.14

def print_area():
    print_circle_area()
    print_rectangle_area()

def print_rectangle_area():
    height = 2.2
    width = 3.4
    area = width * height
    print("Rectangle area is:", area)

def print_circle_area():
    radius = 2.3
    area = PI * radius ** 2
    print("The area of the circle is:", area)

print_area()


#you can output different areas without typing the code multiple times
#make sure to call the radius in he main function, and call it from the first, into the second
#For example
def print_areas():
    radius = 3.2 #creates radius
    print_circle_area1(radius) #stores radius to use in print_circle_area1
    radius = 4.1
    print_circle_area1(radius)

def print_circle_area1(radius): #calls radius from print_area
    area = PI * radius ** 2
    print("The area of the circle is:", area)


print_areas()


#you can also overload variables with other numbers in the main function
#for example
def print_circle_areas():
    rad = 3.1
    print_circle_area2(rad)

def print_circle_area2(radius):
    area = PI * radius ** 2
    print("The area of the circle is:", area)

print_circle_areas()


#this allows for inputting numbers in the termina, and outputting 
#using the inside function
#doesn't work in vscode tho, idk why
def print_power(num, exp):
    power = num ** exp
    print(power)


#boolean value can only be true or false. That's what it's used for
#can make variable like this
my_variable = False
#or use it for finding things
#EX.
6 > 3
6 < 3

#use if else statements. You know what it is
x = 12
if (x < 10):
    print('x is < 10')
    print(x)
    
else:
    print('x is > 10')
    print(x)

    
#use elif to add more else's. its like else if in java
y = 25
if (y == 25):
    print('okay')
    
elif (y > 25):
    print('too high')
    
else:
    print('too low')


#you can imbed if else statements in if else statements
def foo(lol: float):
    if x<0:
        if x<-100:
            print(x/-10)
        else:
            print(x * -1)
        print('1 x is negative')
    else:
        print(x)
    
    
#Truth Tables

#can add not at start of true or flase

#precidence
#not 
#and
#or

#and statements will look at first operation and if it is false, means the second one does not matter and automatically makes it false
#and statements
#true and true = true
#true and false = flase
#false and true = false
#false and false = flase


#or statements will look at frist operation and if it is true, means the second does not matter, and automattically makes it true
#or statements
#true or true = true
#true or flase = true
#false or true = true
#false or false = flase

#ex
def foo(x: float, word: str):
    if word=='GO' and x<0:
        print(x * -1)
    else:
        print(x)
#if not GO, then automatically goes to print(x)
#if GO, then will look at X<0 and display acordingly





#this is basic decimal formatting structure
#general form
#f'{variable_name:Width.decimalplacesf}'
#variable_name=b
#width=8       width is number of spaces between last letter and the number
#decimalplaces=5
b = 27/19
print(f'value of x:{b:8.5f}')


#quiz practice questions
#what is output when name is joe and age is 18
#answer: name: joe, age: 18
def print_details(name: str, age: int):
    print('name: ', name, ', age:', age)


#what to replace ??? with
#print_speed(???)
#need float for decimal answer
def print_speed(dist: float, time: int):
    speed = dist/time
    print(speed)

#what outputs first
#answer is 14 // 12.5
def print_rectangle(width: float, height: float):
    area = width * height
    print(area)

print_rectangle(14 // 12.5, 14 + 3)




