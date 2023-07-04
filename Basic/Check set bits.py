Link : https://practice.geeksforgeeks.org/problems/check-set-bits5408/1?page=3&difficulty[]=-1&status[]=unsolved&sortBy=submissions

Code :

# User function Template for python3

class Solution:
    def isBitSet (self, N):
        if bin(N)[2:].count('1') == len(bin(N)[2:]):
            return 1
        return 0


# Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N = int(input())
        ob = Solution()
        print(ob.isBitSet(N))

# Driver Code Ends
