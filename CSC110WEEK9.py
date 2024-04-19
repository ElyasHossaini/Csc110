#how to open file, which is the first step
# open(filename: str, mode: str) -> TextIO
#mode is r to read
file_handle = open('myfile.txt', 'r')


#read from the file
#basically get all contents of file
# read() -> str
whole_file = file_handle.read()
print(whole_file)

#read file in peices
# readline() -> str
line = file_handle.readline()
#return first line of file
print(line)
#if you repeatidly do this, it will keep printing the next line on after another
#you can do this with a while loop
while line != '':
    print(line)
    line  = file_handle.readline()

#for loop does not output first line

#you can read multiple lines with
# readlines() -> List[str]
#at every position of the list, is one line of the txt file
lines = file_handle.readlines()
print(lines)






#this is how to close the file
file_handle.close()





#how to change a file
#mode is w to write
#w for complete change
#a for append, or adding to end of file
# open(filename: str, mode: str) -> TextIO
#mode is r to read
file_handle = open('myfile.txt', 'w')



#to write a file, use this method
#this comepletly changes the file
#completely overwrites file
# write(text: str) -> int
num_of_chars = file_handle.write('I dont hate niggers')
print(num_of_chars)


file_handle.close()