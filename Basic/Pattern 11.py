Link : https://practice.geeksforgeeks.org/problems/triangle-pattern-1661718455/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=pattern_11

Code :

# User function Template for python3

class Solution:
    def printTriangle(self, N):
        # Code here
        for i in range(1, N+1):
            start = i
            if i % 2 == 1:
                start = 1
            else:
                start = 0
            for j in range(1, i+1):
                print(start, end=" ")
                start = 1 - start
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
