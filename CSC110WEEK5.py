#for loops
'''
following code will print all numbers then print done when it all is done
>>>0
1
2
done
'''
for num in [0,1,2]:
    print(num)
    
print('done')

#loops with range function
#when putting range, goes from first num to last num-1
#ex. range(0,3) prints 0, 1, 2
for num in range(0,3):
    print(num)
    
print('done')

#formula = range(start_num, end_num, interval)
'''
this prints 1,3,5
'''
for num in range(1,6,2):
    print(num)
    
print('done')

'''
output: 7,6,5,4,3,2,1
'''
for num in range (7,0,-1):
    print(num)
print('done')


#accumulator varibale is just adding stuff
'''
>>>output:
num: 1 , sum: 1
num: 2 , sum: 3
num: 3 , sum: 6
done
num: 3 , sum: 6, count: 3
'''
sum = 0
count = 0
for num in range(1,4):
    sum += num
    print('num:', num ,', sum:', sum)
    count += 1
    
print('done')
print('num:', num ,', sum:', sum ,'count:', count)
    


#nested for loops
outer_reps = 10  #this outer for loop loops the inner for loop
'''
output inner for loop:
0 1 2 3!

output for everything
0 1 2 3 !
0 1 2 3 !
0 1 2 3 !
0 1 2 3 !
0 1 2 3 !
0 1 2 3 !
0 1 2 3 !
0 1 2 3 !
0 1 2 3 !
0 1 2 3 !
'''
for outer_num in range(outer_reps):
    reps = 4
    for num in range(reps):
        print(num, end=' ')
    print('!')
    
    
    
#nested loop correlation
'''
output of code when reps = row
row 0 - !
row 1 - 0 !
row 2 - 0 1 !

as you can see, since first row is 0, reps has no value
'''
num_rows = 3
for row in range(num_rows):
    print('row', row, end=' - ')
    reps = row
    for num in range(reps):
        print(num, end=' ')
    print('!')


#when doing nested loops, the total out put is usually the outer * inner. 
#only time it isnt is if in the inner loop, the inner is in the range of the outer
#then u will have to add them to see total number of outputs



#practice problem idk how to solve
for outer in range(3):
    for inner in range(outer):
        print(outer, inner, sep=':', end=' ')
        
'''
the answer is:    1:0 2:0 2:1
BUT IDK WHY
'''