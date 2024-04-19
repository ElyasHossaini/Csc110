
'''
SETUP: The WorldSeriesWinners.csv file contains a chronological
list of the World Series' winning teams from 1903 through 2023.
The data is not necessarily in year order.
(Note the World Series was not played in 1904 or 1994 and so they
have no entry.)
'''

'''
Q1: Design a program that reads this file and 
creates the following 2 dictionaries:
- a dictionary in which the keys are the names of the teams, and each key's
associated value is the years the team has won the World Series
-a dictionary in which the keys are the years, and each key's associated value 
is the name of the team that won that year.
'''
'''
Q2: The program should prompts the user for a year between 1903 through 2022. 
The program should display the name of the team that won the World Series 
that year, and the total number of times that team has won the World Series.
Make sure your program does not crash on bad input.
'''
'''
Q3: The program should also display the most winning teams, 
the number of times they have won, and the years they won
'''
'''
Q4: The program should also display the least winning teams, 
the number of times they have won, and the years they won
'''


#extension - more classes/objects practice:
'''
Q5a: Redo Q1 - Q4 so that instead of using a Dictionary, a list of objects 
is used instead to keep track of each team and the World Series they have won. 
What attributes/field are needed?
(the name of each team and list of years the team won might be a good start)
'''

'''
Q5b: Add a method to the class to determine if the given object
has won the World Series multiple years in a row.
'''


'''
Q5c: Add a method to the class to determine how many different
decades the team has won a World Series in.
'''



'''
Q6:
Design a function called word_count that takes a string as input.
The function should return a dictionary where each unique word in the
string occurs as a key, and the value is the number of times that word 
appeared in the string. You should account for the possibility that 
the string contains punctuation, and might contain both upper and lower
case letters. 

EXAMPLES: 
>>> word_count('')
{}
>>> word_count('the good the bad')
{'the': 2, 'good': 1, 'bad': 1}
>>> word_count('red leather yellow! leather?')
{'red': 1, 'leather': 2, 'yellow': 1}
'''



'''
Q7:
Write a function that takes a filename and returns a dictionary of the
word counts in the given text file. 
You should use the function you wrote in Q2 in this function.
You can test your function on the sample text file provided alongside these questions
'''

def file_word_count(filename: str) -> dict[str, int]:
    """     
    returns a dictionary of word counts in filename ignoring case and puctuation
    -dict[word, number of occurences in text]
    >>> file_word_count('sample.txt')
    {'the': 9, 'words': 1, "hadn't": 1, 'flowed': 1, 'from': 3, 'his': 3, \
'fingers': 1, 'for': 1, 'past': 1, 'few': 1, 'weeks': 1, 'he': 12, 'never': 1, \
'imagined': 1, "he'd": 1, 'find': 1, 'himself': 1, 'with': 4, "writer's": 1, \
'block': 1, 'but': 2, 'here': 1, 'sat': 1, 'a': 2, 'blank': 3, 'screen': 3, \
'in': 2, 'front': 2, 'of': 2, 'him': 2, 'that': 4, 'taunting': 1, 'day': 2, \
'after': 1, 'had': 2, 'started': 1, 'to': 6, 'play': 1, 'mind': 1, "didn't": 1, \
'understand': 1, 'why': 1, "couldn't": 1, 'even': 1, 'type': 1, 'single': 1, \
'word': 1, 'just': 1, 'one': 1, 'begin': 1, 'process': 1, 'and': 3, 'build': 1, \
'there': 1, 'yet': 1, 'already': 1, 'knew': 2, 'eight': 1, 'hours': 1, 'was': 4, \
'prepared': 1, 'sit': 1, 'computer': 1, 'today': 1, 'would': 3, 'end': 1, \
'remaining': 1, 'what': 4, 'supposed': 2, 'do': 3, 'been': 2, 'apparent': 1, \
'beginning': 1, 'made': 1, 'choice': 1, 'so': 1, 'difficult': 1, 'were': 2, \
'not': 1, 'same': 1, 'this': 1, 'have': 1, 'fine': 1, 'if': 1, 'willing': 1, \
'face': 1, 'inevitable': 1, 'consequences': 1, "wasn't": 1}
    """