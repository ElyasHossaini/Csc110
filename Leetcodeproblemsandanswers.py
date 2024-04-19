import math


#two sums problem answer
def twoSum(self, nums: list[int], target: int) -> list[int]:
    prevMap = {}
    
    for i, n in enumerate(nums):
        diff = target - n
        if diff in prevMap:
            return [prevMap[diff], i]
        prevMap[n] = i
    return


#palindrome problem answer. First leetcode
def isPalindrome(x: int) -> bool:
    y = str(x)
    if y[::-1] == y:
        return True   
    else:
        return False
    
    
    
#reverse linked list solution
def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        next = None #used for getting next node
        prev = None #saves the previous node
        
        while head:
            next = head.next #saves next node
            head.next = prev #points to previous node
            prev = head #moves previous node to current node
            head = next #moves head to next node
        return prev #returns the last node


#other tahn searching for the import, solved this one myself. leetcode: addStrings
import sys
sys.set_int_max_str_digits(0)
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        total = int(num1) + int(num2)
        return str(total)
    
    
    
def isValid(s: str) -> bool:
        list_string = list(s)
        num_elements = len(list_string)
        is_t = True
        for index in range(1,num_elements):
            if list_string[index] == list_string[index-1]:
                is_t = True
            else:
                is_t = False
        print(is_t)
isValid('()')