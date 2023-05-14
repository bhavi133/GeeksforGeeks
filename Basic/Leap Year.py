Link : https://practice.geeksforgeeks.org/problems/leap-year0943/1?page=3&difficulty[]=-1&status[]=unsolved&sortBy=submissions

Code :

# User function Template for python3

class Solution:
    def isLeap (self, N):
        if (((N % 4 == 0) and (N % 100 != 0)) or (N % 400 == 0)):
            return 1
        else:
            return 0


# Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N = int(input())
        ob = Solution()
        print(ob.isLeap(N))

# Driver Code Ends
