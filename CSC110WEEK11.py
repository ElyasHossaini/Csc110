#classes-object 
#start by class (Datatype):
class Person:
    '''
    Person with a firstname(fname), last name(lname), and age
    where age >= 0
    '''
    #this is a constructor must name __init__
    def __init__(self, fname: str, lname: str, age: int)-> None:
        '''
        #you implicity call the class and not function
        initialize the attributes of the person self to values passed for fname, lname, and age
        >>> Person('Adanna', 'Ola', 29)
        '''
        #use __ before to make private
        #private vs normal
        #private must make seperate function to return in this example fname
        #normal, you dont need to. 
        #look at line 54 for example
        self.__fname = fname
        self.__lname = lname
        self.age = age
        
        
        
    def set_fname(self, new_name: str) -> None:
        '''
        sets value of fname for Person self to new_name
        >>> aola = Person('Adanna', 'Ola', 29)
        >>> aola.set_name('Jen')
        '''
        self.__fname = new_name
        
    def get_fname(self) -> str:
        '''
        return value of fname for Person self
        >>> aola = Person('Adanna', 'Ola', 29)
        >>> aola.get_fname()
        'Adanna'
        '''
        return self.__fname
    
    def __str__(self) -> str:
        '''
        return an informative string representing the Person self
        '''
        # return self.___fname + ' ' + self.__lname + ': ' + str(self.__age)
        return '{} {} : {}'.format(self.__fname, self.__lname, self.__age)
        
#class and instances are used to make ur own not function but the other thing
#the one where u use a dot. like .append() for example but u use it to basically get stuff
#from tuples easier
aola = Person('Adanna', 'Ola', 29)
print(aola.get_fname(), aola.age)




class Student:
    def __init__(self, sid: str, grade: int) -> None:
        self.__sid = sid
        self.__grade = grade
    
    
    def get_sid(self) -> str:
        return self.__sid
    def get_grade(self) -> int:
        return self.__grade
    def set_grade(self, grade: int) -> None:
        self.__grade = grade

stdnt1 = Student('V00883516', 70)
stdnt2 = Student('V00526859', 91)
print(stdnt1.get_grade(), stdnt2.get_sid())

    
    
