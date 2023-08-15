Link : https://practice.geeksforgeeks.org/problems/minimum-number-in-a-sorted-rotated-array-1587115620/1?page=1&difficulty[]=0&sprint=b177b14354b699a74784fb34752c6a69&sortBy=submissions

Code :

# User function Template for python3

class Solution:
    def minNumber(self, arr,low,high):
        return min(arr)


# Driver Code Starts
# Initial Template for Python 3

import math

def main():
    T=int(input())
    while(T>0): 
        N=int(input())
        A=[int(x) for x in input().strip().split()]
        obj = Solution()
        print(obj.minNumber(A,0,N-1))
        T-=1

if __name__ == "__main__":
    main()

# Driver Code Ends
