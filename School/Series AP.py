Link : https://practice.geeksforgeeks.org/problems/series-ap5310/1?page=1&difficulty[]=-2&status[]=unsolved&sortBy=submissions

Code :

# User function Template for python3

class Solution:
    def nthTermOfAP(self,A1,A2,N):
        common_difference = (A2 - A1)
        x = A1
        for i in range(N-1):
            x = x + common_difference
        return x

 
# Driver Code Starts
# Initial Template for Python 3

if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        A1,A2,N=map(int,input().strip().split(' '))
        ob=Solution()
        print(ob.nthTermOfAP(A1,A2,N))  

# Driver Code Ends
