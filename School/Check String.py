Link : https://practice.geeksforgeeks.org/problems/check-string1818/1?page=1&difficulty[]=-2&status[]=unsolved&sortBy=submissions

Code :

# User function Template for python3

class Solution:
    def check (self,s):
        return len(list(set(s))) == 1


# Driver Code Starts
# Initial Template for Python 3

t = int (input ())
for tc in range (t):
    s = input ()
    ob = Solution()
    if ob.check (s):
        print ("YES")
    else:
        print ("NO")
        
# Driver Code Ends
