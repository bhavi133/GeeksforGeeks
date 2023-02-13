Link : https://practice.geeksforgeeks.org/problems/binary-array-sorting-1587115620/1?page=1&difficulty[]=-2&difficulty[]=-1&status[]=unsolved&sortBy=submissions

Code :

# User function Template for python3

class Solution:
    
    #Function to sort the binary array.
    def binSort(self, A, N): 
        return A.sort()
        #Your code here
        #No need to print the array
    

# Driver Code Starts
# Initial Template for Python 3

import math

def main():
        T=int(input())
        while(T>0):
            N=int(input())
            A=list(map(int,input().split()))
            obj = Solution()
            obj.binSort(A,N) 
            for i in A:
                print(i,end=" ")
            print()
            T-=1

if __name__ == "__main__":
    main()
# Driver Code Ends
