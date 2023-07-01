Link : https://practice.geeksforgeeks.org/problems/abset-25327/1?page=2&difficulty[]=1&status[]=unsolved&sortBy=submissions

Code :

# User function Template for python3

class Solution:
    def power (self, a, b):
        return pow(a, b, 10**9+7)


# Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        a, b = map(int,input().split())
        ob = Solution()
        print(ob.power(a, b))

# Driver Code Ends
