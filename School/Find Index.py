Link : https://practice.geeksforgeeks.org/problems/find-index4752/1?page=2&difficulty[]=-2&sortBy=submissions

Code :

# User function Template for python3

class Solution:
    def findIndex (self,a, N, key):
        l = []
        for i in range(N):
            if a[i] == key:
                l.append(i)
                
        if len(l) >= 1:
            return min(l), max(l)
        else:
            return [-1, -1]

            
# Driver Code Starts
# Initial Template for Python 3

t=int(input())
for _ in range(0,t):
    n=int(input())
    a=list(map(int,input().split()))
    key=int(input())
    ob = Solution()
    ans=ob.findIndex(a, n, key )
    print(*ans)
    
# Driver Code Ends
