Link : https://practice.geeksforgeeks.org/problems/disarium-number1045/1?page=2&difficulty[]=-1&sprint=b177b14354b699a74784fb34752c6a69&sortBy=submissions

Code :

# User function Template for python3

class Solution:
    def isDisarium(self, N):
        arr = list(map(int, str(N)))
        sum = 0
        for i, j in enumerate(arr):
            sum += pow(j, i+1)
        
        if sum == N:
            return 1
        return 0


# Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N = int(input())
        ob = Solution()
        print(ob.isDisarium(N))

# Driver Code Ends
