#This is how to output words. Make sure to use quotations
print("Hello world");

#you can also output numberts as well with the print function
print(2);

#use opertators with numbers to do basic math(+ - * / % //(This outputs the whole number if you divide something that gets a decimal))
print(3 + 5);
print(5 - 3);
print(5 * 3);
print(6 / 2);
print(5 % 2);
print(5 // 2);

#use variables and variable types to store info
#str holds strings/words
#int holds whole numbers with no decimal
#float holds numbers with decimals
Word = "Hey guys "
print(Word);

x = 5
print(x);

y = 6
print(y);

z = 3.0
print(z);

#you can use operators on these useing the given variable
print(x + y);

print(x * y);

#if you use operators with 2 differnet variable types, i.e. int and float, the answer will be a float variable
print(x + z)

print(x * z)

#you can also multiply str with int to display the number of words you multiply by. Can't multiply float and str
print(Word * x)

#you can also do use operators with writing full code using (var += 3) ect.
#formula is var = var + 3
x += 3
print(x)

Word *= 6
print(Word)

#use escape sequences to output certain items
#\n to print on a new line
#\t to force output to print a tab
#\' to force a single quotation to print
#\" to force a double quote to print
#\\ forces backslash to print
print("Hey guys, you\'re going to love this.\n\"Get yo ass down here\"\nDamn")

#use the def method to make your own function
#cant use def to call things above it, only under the code
#use to make coding look nicer
def my_name():
    print("I love money!")

my_name()

#you can use make something like a call type function to print things easier
#now it does everything just with one function instead of two
def call_function():
    my_function()
    print_name()

def my_function():
    r = 2
    r *= 4
    print(r)

def print_name():
    name = "Elyas"
    print(name)

call_function()

#you can also add constants to the top of code so that you don not have to keep adding it
EMPLOYEE_DISCOUNT = 0.25

def print_discount():
    cost = 10.28
    amount = cost * EMPLOYEE_DISCOUNT
    print(amount)

print_discount()