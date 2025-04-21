'''
Write a Python program to generate a Palindrome Triangle up to a given number of rows.
 The Palindrome Triangle is a symmetrical pattern where each row forms a palindrome,
   extending with consecutive numbers to the midpoint and then decreasing back to 1.
 
Input: An integer n representing the number of rows in the triangle.
 
Output: Print the Palindrome Triangle with n rows, aligning the numbers to form a symmetrical pattern.
 
Example:
Input: 5 
Explanation: The output displays a Palindrome Triangle with 5 rows. Each row is symmetric and forms a palindrome, starting and ending with 1, with the numbers increasing towards the center of the row.
 
Constraints: 
1 ≤ n ≤ 10

Acceptance Criteria:
Ensure your output matches the format shown in the example, with each row of the triangle centered according to the number of digits in the last row.
Ensure your algorithm achieves O(n) time complexity, where n is the number of rows in the pattern. 
[Hint] Appearance can be deceiving, it not just related to loops. There might be a mathematical formula that you can use to generate the number. Your algorithm, Your Choice 😊


'''

def Triangle(n):
    if not (1 <=n<= 10):
        print("the num not accepted")
        return
    for i in range(1,n+1):
        left=list(range(1,i+1))
        right=list(range(i-1,0,-1))
        row =left+right
        print(row)


Triangle(5)