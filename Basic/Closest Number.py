Link : https://practice.geeksforgeeks.org/problems/closest-number5728/1?page=1&difficulty[]=-1&status[]=unsolved&sortBy=submissions

Code :

# User function Template for python3

class Solution:
    def closestNumber(self, N , M):
        q = N // M
        x = q * M
        y = (q + 1) * M
        if abs(N - x) < abs(N - y):
            return x
        else:
            return y


# Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N,M=map(int,input().split())      
        ob = Solution()
        print(ob.closestNumber(N,M))

# Driver Code Ends
