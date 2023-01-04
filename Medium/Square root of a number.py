Link : https://practice.geeksforgeeks.org/problems/square-root/1?page=1&difficulty[]=1&status[]=solved&sortBy=submissions

Code :

#User function Template for python3

import math

class Solution:
    def floorSqrt(self, x): 
        square = int(math.sqrt(x))
        if (square * square) == x:
            return square
        else:
            return square


# Driver Code Starts
# Initial Template for Python 3

import math

def main():
        T=int(input())
        while(T>0):            
            x=int(input())
            print(Solution().floorSqrt(x))
            T-=1
if __name__ == "__main__":
    main()
# Driver Code Ends
