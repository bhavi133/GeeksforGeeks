Link : https://practice.geeksforgeeks.org/problems/nth-fibonacci-number1335/1?page=1&difficulty[]=0&status[]=solved&sortBy=submissions

Code :

#User function Template for python3

class Solution:
    def nthFibonacci(self, n):
        l = [0,1]
        if n == 1:
            return 0
        if n == 2: 
            return 1
        else:
            for i in range(n-1):
                l.append(l[i] + l[i+1])
            return l[n] % 1000000007
            

# Driver Code Starts
# Initial Template for Python 3

import sys
sys.setrecursionlimit(10**6)

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        n = int(input())      
        ob = Solution()
        print(ob.nthFibonacci(n))
# Driver Code Ends
