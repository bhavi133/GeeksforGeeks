Link : https://practice.geeksforgeeks.org/problems/mind-game3637/1?page=2&difficulty[]=-1&status[]=unsolved&sortBy=submissions

Code :

# User function Template for python3

class Solution:
    def mindGame(self, K):
        for i in range(1, 11):
            w = i * 2
            x = w + K
            y = x // 2
            z = y - i
        return z


# Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        K=int(input())   
        ob = Solution()
        print(ob.mindGame(K))

# } Driver Code Ends
