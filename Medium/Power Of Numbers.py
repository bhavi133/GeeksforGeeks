Link : https://practice.geeksforgeeks.org/problems/power-of-numbers-1587115620/1?page=2&difficulty[]=1&status[]=unsolved&sortBy=submissions

Code :

# User function Template for python3

class Solution:
    def power(self,N,R):
        return pow(N, R, 10**9+7)
        

# Driver Code Starts
# Initial Template for Python 3

import math

def main():  
    T=int(input())
    while(T>0):
        N=input()
        R=N[::-1]
        ob=Solution();
        ans=ob.power(int(N),int(R))
        print(ans)
        T-=1

if __name__=="__main__":
    main()

# Driver Code Ends
