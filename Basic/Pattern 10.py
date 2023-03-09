Link : https://practice.geeksforgeeks.org/problems/triangle-pattern-1661718013/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=pattern_10

Code :

# User function Template for python3

class Solution:
    def printTriangle(self, N):
        # Code here
        for i in range(1, (2*N-1)+1):
            stars = i
            if (i > N):
                stars = (2*N-i)
            for j in range(1, stars+1):
                print('*', end=" ")
            print()


# Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input().strip())
        ob = Solution()
        ob.printTriangle(N)

# Driver Code Ends
