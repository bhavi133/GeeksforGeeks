Link : https://practice.geeksforgeeks.org/problems/square-pattern/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=pattern_1

Code :

# User function Template for python3

class Solution:
    def printSquare(self, N):
        for row in range(N):
            for col in range(N):
                print('*', end=" ")
            print()


# Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        ob = Solution()
        ob.printSquare(N)

# Driver Code Ends
