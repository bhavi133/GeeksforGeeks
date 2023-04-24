Link : https://practice.geeksforgeeks.org/problems/sum-of-first-n-terms5843/1?page=3&difficulty[]=-1&status[]=unsolved&sortBy=submissions

Code :

# User function Template for python3

class Solution:
    def sumOfSeries(self,N):
        return ((N*(N+1)//2)**2)


# Driver Code Starts
# Initial Template for Python 3

if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        N=int(input())
        ob=Solution()
        print(ob.sumOfSeries(N)) 

# Driver Code Ends
