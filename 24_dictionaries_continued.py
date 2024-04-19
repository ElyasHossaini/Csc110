import doctest


''' Q1. Create and return an inverted version of a
dictionary of type dict[str, int] passed as an argument.
Each unique value in the input dictionary becomes a key in the output dictionary.
'''


'''
Q2. Imagine you have a file filled with rows of restaurant data, 
where each row has the following information, separated by commas :
- the restaurant name
- the rating of that restaurant
- a number of dollar signs representing the price point of that restaurant
- the types of food served by that restaurant (at least one)
(see sample text file provided: restaurant_data.txt)

Problem Description
You want to write a recommender function (with necessary helper functions) 
that will allow someone to specify: 
the name of the input file holding the restaurant data, 
the price they want to pay 
and a set of food types they are interested in.

The program should find all the restaurants that are at 
that price point and that serve at least one of the food types 
the person is interested in.
The program should give them a list of the restaurant names with their ratings, 
in order of increasing rating.

Not sure where to start...
1. Work through an example
- What inputs (arguments) should the function take?
- What should the function output (return)?

2. Where should you store the data as it is read in from the file?
- what items within a line of data would it be useful to filter on? 
  By filter we mean, which items within a line of the data should be 
  considered to decide if the restaurant on that line of data should be 
  included in the report to the user.
- What dictionaries will you want your program to create to help 
  with filtering the data.
  Think about what you want to filter on, and what you want to produce.
  -> What you filter on is the key and what you produce is the value.
  
3. What steps will your program need to perform to solve this problem? 
'''