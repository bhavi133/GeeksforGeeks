Link : https://practice.geeksforgeeks.org/problems/floyds-triangle1222/1?page=2&difficulty[]=-2&status[]=unsolved&sortBy=submissions

Code :

# User function Template for python3

class Solution:
    def printFloydTriangle(self, N):
    	x = 1
    	for i in range(1, N+1):
    	    for j in range(1, i+1):
    	        print(x, end=" ")
    	        x += 1
    	    print()


# Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        N = int(input())
        ob = Solution()
        ob.printFloydTriangle(N)
        
# Driver Code Ends
