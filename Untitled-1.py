"""
INPUT:
num_of_rows = 5
OUTPUT: (Please don't multiply a string with integer)
*****
*****
*****
*****
*****
"""



#for i in range(5):
#    print("******")



'''INPUT:
num_of_rows = 5
OUTPUT: (Please don't multiply a string with integer)
*
***
*****
*******
*********
"""
"""'''
#in_num=5
#for i in range(in_num):
#    for j in range(2 *i +1 ):
#        print("*", end="")
#    print()

'''
INPUT:
num_of_rows = 5
OUTPUT: (Please don't multiply a string with integer)
    *
   ***
  *****
 *******
*********
'''


#in_num = 5
#for i in range(in_num):
    # Print spaces before the stars
#    for space in range(in_num - i - 1):
#        print(" ", end="")

    # Print the stars
#    for j in range(2 * i + 1):
#        print("*", end="")

    # Move to the next line
 #   print()#
'''

Write a Python program that takes an integer input for the size of the square and prints a hollow 
square pattern using asterisks (*). The border of the square should be made of asterisks, and the
inside of the square should be hollow (filled with spaces).
 
Input: An integer size representing the length of the sides of the square.
 
Output: Print a hollow square made of asterisks with the length of each side equal to size.
 
Example:
 
Input: 5 
 
Output:
 

 
Explanation: The output displays a hollow square pattern with each side having a length of 5 units. 
The border of the square is composed of asterisks, while the inside of the square is hollow, filled 
with spaces.
 
 
Constraints:
2 ≤ size ≤ 20
 
 
Acceptance Criteria:
The square must have a border of asterisks, with the inside hollow except for the border.
 
Use loops efficiently to minimize the complexity of your solution.
 
Ensure your algorithm achieves O(n) time complexity, where n is the number of rows (size) in the pattern. 
 
[Hint] Think of a way to utilize Python list comprehension and list slicing concept to implement the solution in O(n) time.

'''

#n=int(input("enter the size"))

def hollow(n):
    if not (2 <= n <= 20):
        print("Size must be between 2 and 20.")
        return
    else:
        for i in range(n):
            if i==0 or i==(n-1):
                print("*"*n)
            else:
                print("*", " "*(n-2) ,"*")


#hollow(n)

rnum=3
cnum=3
count= 1
for i in range(rnum):
    for j in range(cnum):
        print(count ,end="")
        count+=1
    print()

