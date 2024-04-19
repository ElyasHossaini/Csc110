#lsit mutability
def foo() -> None:
    vals = [1,2,3]
    print(vals)
    
    bar(vals)
    print(vals)
    
def bar(nums: list[int]) -> None:
    num_elements  = len(nums)
    for index in range(num_elements):
        nums[index] = nums[index] * 2
    
    print(nums)
foo()
#output:
# [1, 2, 3]
# [2, 4, 6]
# [2, 4, 6]




#list copy
def doo(Ion: list[int]) -> None:
    new_list = []
    
    
    for n in Ion:
        new_list.append(n+1)
        
    for index in range(len(Ion)):
        Ion[index] = new_list[index]
        
I = [2,3,4]
doo(I)
print(I)
#output:
# [1, 2, 3]
# [2, 4, 6]
# [2, 4, 6]
# [3, 4, 5]