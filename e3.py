'''
You are given a list of integers and a target sum. Write a Python function that finds all
 unique pairs of numbers in the list that add up to the target sum. The function should 
 return a list of tuples, each containing a pair of numbers. If no such pairs exist, the 
 function should return an empty list.

Function Signature: 
def find_target_sum(nums, target):
Inputs:
nums: A list of integers.
target: An integer representing the target sum.
 
Output:
A list of tuples, each tuple containing two integers that add up to the target sum. If no such pairs exist, return an empty list.
Example 1:
Input: nums = [2, 7, 11, 15, -2], target = 9
Output: [(2, 7), (-2, 11)]
Explanation: The numbers 2 and 7, as well as -2 and 11, add up to 9, which is the target sum.


Constraints:
The list nums will have at least 2 and at most 1000 elements.
Each element in the list will be an integer ranging from -10^9 to 10^9.
The target sum will be an integer ranging from -10^9 to 10^9.
 
Notes:
A number can be used in multiple pairs.
Pairs should be unique; for example, [1, 2] and [2, 1] are considered the same pair and should only be counted once.
The function should handle duplicates in the input list appropriately.
Nested loops are not allowed. Ensure your algorithm achieves O(n) time complexity, where n is the number of integers in nums list. 
[Hint] Consider using a data structure that can optimize and simplify the algorithm.
'''

def find_target_sum(nums, target):
    x=set()
    outPairs=set()

    for i in nums:
        toTarget = target - i
        if toTarget in x:
            pair = tuple(sorted((i, toTarget)))
            outPairs.add(pair)
        x.add(i)
    return list(outPairs)

nums = [2, 7, 11, 15, -2]
target = 9

#nums = [1, 5, 3, 8]
#target = 12
print(find_target_sum(nums, target))
