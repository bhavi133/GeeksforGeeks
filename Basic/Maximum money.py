Link : https://practice.geeksforgeeks.org/problems/maximum-money2855/1?page=2&difficulty[]=-1&status[]=unsolved&sortBy=submissions

Code :

# User function Template for python3

class Solution:
    def maximizeMoney(self, N , K):
        return (N - (N // 2)) * K


# Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N,K = map(int,input().split())      
        ob = Solution()
        print(ob.maximizeMoney(N,K))

# Driver Code Ends
