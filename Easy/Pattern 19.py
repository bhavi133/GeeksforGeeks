Link : https://practice.geeksforgeeks.org/problems/double-triangle-pattern/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=pattern_19

Code :

# User function Template for python3

class Solution:
    def printTriangle(self, N):
        # Code here
        for i in range(1, N+1):
            for j in range(1, (N-i+1)+1):
                print('*', end="")
            
            for j in range(1, (2*i-2)+1):
                print(' ', end="")
                
            for j in range(1, (N-i+1)+1):
                print('*', end="")
                
            print()
            
        for i in range(1, N+1):    
            for j in range(1, i+1):
                print('*', end="")
            
            for j in range(1, (2*N-2*i)+1):
                print(' ', end="")
                
            for j in range(1, i+1):
                print('*', end="")
                
            print()

# Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input().strip())
        ob = Solution()
        ob.printTriangle(N)

# Driver Code Ends
