import doctest


''' Q1. In this problem, assume we have a file called yvrTemperatures08.txt
containing the temperature readings at Vancouver International Airport at
midnight, 6am, noon and 6pm on given days of the year 2008.
The meteorologists at the airport attempt to record data every day but
technical problems mean that data for some days of the year could go missing.
We know the file is formatted as follows:
- data for each day is on a line of its own
- the first entry is an integer from 1 to 366 (2008 was a leap year)
representing the day of the year
- the next four entries are floating point numbers representing the temperature at
midnight, 6am, noon and 6pm, in that order
- there is at least one line of data in the file

STEP 1: work through an example

Given the sample data file below:
1. Calculate the average temperature at
midnight, at 6am, at noon and 6pm across the days

2. For each time (midnight, at 6am, at noon and 6pm), count the number of
readings that are above the calculated average for that time of day

1    3.4  2.3  3.5  5.4
74   1.2  1.2  2.3  2.2
298  -2.1 -0.1 1.0  0.5
366  1.3  1.3  2.4  2.1



STEP 2: Given your process for completing the above calculations,
design a program that, given the weather data in the file, prints
the average temperatures for the 4 times of day and the number of readings
across all days that are above the calculated average for each of the 4 times.

Think about what functions you will need to write.
Reading from a file is time consuming,
so make sure your design will only read from the file once!

What does the data you need to store look like?
Which function will you write first?
Which functions will need to call other functions?

Extension:  Write your results to an output file.
'''
