import doctest
from pet import Pet
from date import Date

'''
Q1 - add the method set_name to the Pet class
The method should take a name as an argument and 
update the Pet's name to the given name
'''

'''
Q2 - objects are mutable...
'''
def q2() -> None:
    p1 = Pet('Rover', 'Dog', Date(12, 31, 2010))
    p2 = Pet('Red', 'Cat', Date(9, 15, 2016))
    p3 = Pet('Chewie', 'Hamster', Date(1, 23, 2009))
    pets = [p1, p2, p3]
    #add code to change the names of all Pet instances in pets to 'unnamed'
    

    #print the pets list - what will the output be?
    
    
    #print the p1, p2 and p3 - what will the output be?
    
    
    #add code to change the name of p1 to 'Sandy'
    
    
    #print p1, p2 and p3 - what will the output be?
    
    
    #print the pets list - what will the output be? 
    
    
'''
Q3 - practice creating classes...
Design a new class called SPCA that has 2 fields/attributes:
-a city name
-a list of Pet instances

add/test the following methods in your class:
__init__
__str__
__repr__
__eq__
get_pets_of_species: 
  takes a species and return a list of all the pets of that species in this SPCA
'''
    

'''
Q4:
Create a Student class that contains the following attibutes (or fields):
the name, major, and average grade of a given student. 
Names and majors should be of type string. 
Averages should be represented by floating point numbers. 
Create 3 student objects (or instances) using your Student class.
'''


'''
Q5:
Design a function called get_academic_standing that returns a 
student's academic standing as a string based on their 
average. This function should also be part of the Student class. 
average < 50.0 = "poor academic standing"
50.0 <= average < 60.0 = "academic probation"
average >= 60.0 = "good academic standing"

Finally, get the academic standings of the 3 students you created earlier. 
'''
