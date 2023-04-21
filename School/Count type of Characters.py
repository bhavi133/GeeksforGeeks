Link : https://practice.geeksforgeeks.org/problems/count-type-of-characters3635/1?page=1&difficulty[]=-2&status[]=unsolved&sortBy=submissions

Code :

# User function Template for python3

class Solution:
    def count (self,s):
        uppercase_characters = 0
        lowercase_characters = 0
        numeric_characters = 0
        special_characters = 0
        l = []
        for i in s:
            if i.isupper():
                uppercase_characters += 1
            elif i.islower():
                lowercase_characters += 1
            elif i.isnumeric():
                numeric_characters += 1
            else:
                special_characters += 1
        
        return [uppercase_characters, lowercase_characters, numeric_characters, special_characters]
        
   
# Driver Code Starts
# Initial Template for Python 3

t = int (input ())
for tc in range (t):
    s = input ()
    ob = Solution()
    res = ob.count (s)    
    for i in res:
        print (i)
    
# Driver Code Ends
