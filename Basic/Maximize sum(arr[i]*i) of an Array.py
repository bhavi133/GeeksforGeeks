Link : https://practice.geeksforgeeks.org/problems/maximize-arrii-of-an-array0026/1?page=1&difficulty[]=-1&status[]=unsolved&sortBy=submissions

Code :

# User function Template for python3

class Solution:
    def Maximize(self, a, n): 
        # Complete the function
        ctr = 0
        arr = sorted(a)
        for i, j in enumerate(arr):
            ctr = ctr + i * j
        return ctr % 1000000007
      

# Driver Code Starts
# Initial Template for Python 3

for _ in range(0,int(input())):
    n = int(input())
    arr = list(map(int,input().strip().split()))
    ob=Solution()
    print(ob.Maximize(arr, n))
    
# Driver Code Ends
