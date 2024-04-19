import doctest

class Student:
    """ Student with unique id (sid) and current grade (grade)"""

    def __init__(self, sid: str, grade: int) -> None:
        """ initializes an instance of a Student with sid and grade
        >>> stdnt = Student('V00123456', 89)
        """
        self.__sid = sid
        self.__grade = grade

    def __str__(self) -> str:
        """ return a formatted string with sid and grade of self Student
        >>> stdnt = Student('V00123456', 89)
        >>> str(stdnt)
        'V00123456: 89/100'
        """
        return f'{self.__sid}: {self.__grade}/100'

    def __repr__(self) -> str:
        """ return a formatted string  with student attributes
        >>> stdnt = Student('V00123456', 89)
        >>> stdnt
        Student('V00123456', 89)
        """        
        return f'Student({repr(self.__sid)}, {repr(self.__grade)})'
    
    # TODO: add documentation for these instance methods
    def get_sid(self) -> str:
        '''
        return value of sid in Student self
        >>> stdnt = Student('V0495049', 56)
        >>> stdnt.get_sid()
        'V0495049'
        '''
        return self.__sid

    def get_grade(self) -> int:
        '''
        return value of grade in Student self
        >>> stdnt = Student('V839498', 89)
        >>> stdnt.get_grade()
        89
        '''      
        return self.__grade

    def set_grade(self, grade) -> None:
        '''
        sets the value of grade for Student self to grade
        >>> stdnt = Student('V039480', 98)
        >>> stdnt.set_grade(87)
        '''
        self.__grade = grade
    
    def __eq__(self, other: 'Student') -> bool:
        """ returns True if sid of self and other are equal
        >>> stdnt1 = Student('V00123456', 89)
        >>> stdnt1_eq = Student('V00123456', 89)
        >>> stdnt1_noteq = Student('V00123457', 89)
        >>> stdnt1 == stdnt1
        True
        >>> stdnt1 == stdnt1_eq
        True
        >>> stdnt1 == stdnt1_noteq
        False
        """
        return self.__sid == other.get_sid()
    
    def is_grade_above(self, threshold: int) -> bool:
        '''
         takes as arguments a self-reference to the Student instance 
         (self) and an additional argument as a threshold grade. The method
         should determine whether the grade of self is above the given threshold grade.
         >>> stdnt1 = ('V985953', 98)
         >>> stdnt2 = ('V938940', 23)
         >>> stdnt1.is_grade_above(67)
         True
         >>> stdnt2.is_grade_above(67)
         False
        '''
        return self.__grade > threshold
