Link : https://practice.geeksforgeeks.org/problems/adam-number2650/1?page=2&difficulty[]=-1&sprint=b177b14354b699a74784fb34752c6a69&sortBy=submissions

Code :

# User function Template for python3

class Solution:
    def checkAdamOrNot(self, N):
        x = N ** 2
        y = int(str(N)[::-1]) ** 2
        if x == int(str(y)[::-1]):
            return 'YES'
        return 'NO'


# Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N = int(input())
        ob = Solution()
        print(ob.checkAdamOrNot(N))

# Driver Code Ends
