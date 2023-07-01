Link : https://practice.geeksforgeeks.org/problems/find-maximum-number2152/1?page=2&difficulty[]=1&status[]=unsolved&sortBy=submissions

Code :

# User function Template for python3

class Solution:
    def findMax(self, N):
        return "".join(sorted(list(N), reverse=True))


# Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N=input()       
        ob = Solution()
        print(ob.findMax(N))

# Driver Code Ends
