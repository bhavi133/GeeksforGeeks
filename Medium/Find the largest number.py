Link : https://practice.geeksforgeeks.org/problems/find-the-largest-number4953/1

Code :

# User function Template for python3

class Solution:
    def find (self, N):
        for i in range(N, -1, -1):
            if i == int("".join(sorted(str(i)))):
                return i


# Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N = int(input())
        ob = Solution()
        print(ob.find(N))

# Driver Code Ends
