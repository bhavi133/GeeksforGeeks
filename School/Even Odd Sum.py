Link : https://practice.geeksforgeeks.org/problems/even-odd-sum5450/1?page=1&difficulty[]=-2&status[]=unsolved&sortBy=submissions

Code :

# User function Template for python3

class Solution:
    def EvenOddSum(self,N,Arr):
        even_sum = 0
        odd_sum = 0
        l = []
        for i in range(N):
            if i % 2 == 0:
                odd_sum += Arr[i]
            else:
                even_sum += Arr[i]
        return [odd_sum, even_sum]


# Driver Code Starts
# Initial Template for Python 3

if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        N=int(input())
        Arr=list(map(int,input().strip().split(' ')))
        ob=Solution()
        ans=ob.EvenOddSum(N,Arr)
        print(ans[0],end=" ")
        print(ans[1])

# Driver Code Ends
