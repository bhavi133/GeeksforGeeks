Link : https://practice.geeksforgeeks.org/problems/find-n-th-term-of-series-1-3-6-10-15-215506/1?page=1&difficulty[]=-2&status[]=unsolved&sortBy=submissions

Code :

# User function Template for python3

class Solution:
    def findNthTerm(self, N):
        return N * (N + 1) // 2
        

# Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N=int(input())      
        ob = Solution()
        print(ob.findNthTerm(N))

# Driver Code Ends
