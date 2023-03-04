Link : https://practice.geeksforgeeks.org/problems/right-triangle/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=pattern_2

Code :

# User function Template for python3

class Solution:
    def printTriangle(self, N):
        # Code here
        for row in range(1, N+1):
            for col in range(N+row-N):
                print('*', end=" ")
            print()


# Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        ob = Solution()
        ob.printTriangle(N)
        
# Driver Code Ends
