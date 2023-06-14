Link : https://practice.geeksforgeeks.org/problems/find-first-set-bit-1587115620/1?page=3&difficulty[]=0&status[]=unsolved&sortBy=submissions

Code :

# Driver Code Starts
# Initial Template for Python 3

import math

# Driver Code Ends
# User function Template for python3

class Solution:  
    def getFirstSetBit(self,n):
        binary_string = bin(n)[2:]
        if '1' in binary_string:
            return binary_string[::-1].index('1') + 1
        return 0
        
# Driver Code Starts.
    
def main():    
    T=int(input())
    while(T>0):        
        n=int(input())
        ob=Solution()
        print(ob.getFirstSetBit(n))
        T-=1
    
if __name__=="__main__":
    main()
# Driver Code Ends
