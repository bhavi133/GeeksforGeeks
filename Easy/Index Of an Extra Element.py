Link : https://practice.geeksforgeeks.org/problems/index-of-an-extra-element/1?page=8&difficulty[]=0&difficulty[]=1&status[]=unsolved&sortBy=submissions

Code :

class Solution:
    def findExtra(self,a,b,n):
        return a.index(list(set(a)-set(b))[0])
        # return a.index(list(set(a).difference(set(b)))[0])

# Driver Code Starts

if __name__ == "__main__":
    t=int(input())
    for i in range(t):
        n=int(input())
        a=list(map(int,input().split()))
        b=list(map(int,input().split()))
        print(Solution().findExtra(a,b,n))

# Driver Code Ends
