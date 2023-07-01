Link : https://practice.geeksforgeeks.org/problems/count-digits-in-a-factorial3957/1?page=2&difficulty[]=1&status[]=unsolved&sortBy=submissions

Code :

# User function Template for python3

import math

class Solution:
    def facDigits(self,N):
        # fact = math.factorial(N)
        # l = list(str(fact))
        # return len(l)
        
        return len(list(str(math.factorial(N))))


# Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N = int(input())
        ob = Solution()
        print(ob.facDigits(N))

# Driver Code Ends
