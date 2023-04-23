Link : https://practice.geeksforgeeks.org/problems/mean0021/1?page=1&difficulty[]=-2&status[]=unsolved&sortBy=submissions

Code :

# User function Template for python3

class Solution:
    def mean(self, N , A):
        return sum(A) // N


# Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N=int(input())
        A = list(map(int,input().split()))    
        ob = Solution()
        print(ob.mean(N,A))

# Driver Code Ends
