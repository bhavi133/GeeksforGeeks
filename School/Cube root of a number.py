Link : https://practice.geeksforgeeks.org/problems/cube-root-of-a-number0915/1?page=2&difficulty[]=-2&status[]=unsolved&sortBy=submissions

Code :

# User function Template for python3

class Solution:
    def cubeRoot(self, N):
        return int(N ** (1/3))
        
 
# Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N = int(input())      
        ob = Solution()
        print(ob.cubeRoot(N))

# Driver Code Ends
