Link : https://practice.geeksforgeeks.org/problems/ncr1019/1?page=1&difficulty[]=1&status[]=solved&sortBy=submissions
  
Code : 
  
#User function Template for python3

import math

class Solution:
    def nCr(self, n, r):
        y = 1000000007
        if r > n:
            return 0
        else:
            x = (math.factorial(n)) // (math.factorial(r) * math.factorial(n-r))
            return x % y


# Driver Code Starts
import sys
sys.setrecursionlimit(10**6)

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n, r = [int(x) for x in input().split()]
        
        ob = Solution()
        print(ob.nCr(n, r))
# Driver Code Ends
