Link : https://practice.geeksforgeeks.org/problems/triangle-number-1661489840/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=pattern_6

Code :

# User function Template for python3

class Solution:
    def printTriangle(self, N):
        # Code here
        for i in range(1, N+1):
            for j in range(1, (N-i+1)+1):
                print(j, end=" ")
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
