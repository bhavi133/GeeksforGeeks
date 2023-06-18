Link : https://practice.geeksforgeeks.org/problems/pattern-printing1347/1?page=1&difficulty[]=-2&status[]=unsolved&sortBy=submissions

Code :

# User function Template for python3

class Solution:
    def printPattern(self, N):
    	for i in range(1, N+1):
    	    print('*'*i, end=" ")
    	    
      # for i in range(N):
      #     for j in range(i+1):
      # 	      print('*', end="")
      #     print(end=" ")


# Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        N = int(input())
        ob = Solution()
        ob.printPattern(N)
        print()

# Driver Code Ends
