Link : https://practice.geeksforgeeks.org/problems/smallest-positive-missing-number-1587115621/1?page=1&difficulty[]=1&status[]=unsolved&sortBy=submissions

Code :

# User function Template for python3

class Solution:
    def missingNumber(self,arr,n):
        l = set(arr)
        for i in range(1, n+2):
            if i not in l:
                return i


# Driver Code Starts
# Initial Template for Python 3

import math

def main():
        T=int(input())
        while(T>0):            
            n=int(input())
            arr=[int(x) for x in input().strip().split()]
            ob=Solution()
            print(ob.missingNumber(arr,n))
            T-=1

if __name__ == "__main__":
    main()

# Driver Code Ends
