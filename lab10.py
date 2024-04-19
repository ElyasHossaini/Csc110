import doctest
import student

SID = 0
GRADE = 1



def get_students(filename: str) -> list[object]:
    '''
     takes a name of a file and creates and returns a new list of Student
     instances (objects) using the data in filename
    '''
    file_handle = open(filename, 'r', encoding='utf8')
    line = file_handle.readline()
    final_list = []
    while line != '':
        sid_and_grade = line.split(',')
        final_list.append(student.Student(sid_and_grade[SID], sid_and_grade[GRADE]))
        line = file_handle.readline()
    file_handle.close()
    return final_list


def get_classlist(list_student_objects: list[object]) -> list[str]:
    '''
    takes a list of Student instances and creates and returns a new list of just
    the student ids of all Student instances in the list.
    '''
    final_list = []
    num_elements = len(list_student_objects)
    for index in range(num_elements):
        final_list.append(list_student_objects[index].get_sid())
    return final_list

def count_above(list_student_objects: list[object], threshold: int) -> int:
    '''
    takes a list of Student instances and an additional argument as a threshold grade. 
    The function should return a count of the number of Student instances in the list 
    that have a grade above the given threshold grade.
    '''
    # list_grades = []
    num_elements = len(list_student_objects)
    count = 0
    for index in range(num_elements):
        if list_student_objects[index].is_grade_above(threshold) == True:  
            count += 1
        # list_grades.append(list_student_objects[index].get_grade())
    # num_elements_list_grades = len(list_grades)
    # for index in range(num_elements_list_grades):
    #     if list_grades[index] > threshold:
    #         count += 1
    return count

def get_average_grade(list_student_objects: list[object]) -> float:
    '''
    takes a list of Student instances. The function should calculate and return the average grade
    of all Student instances in the list as a floating point number.
    '''
    list_grades = []
    num_elements = len(list_student_objects)
    total_num = 0
    count = 0
    for index in range(num_elements):
        list_grades.append(list_student_objects[index].get_grade())
    
    num_elements_list_grades = len(list_grades)
    for index in range(num_elements_list_grades):
        total_num += list_grades[index]
        count += 1
    
    average = total_num / count
    return average