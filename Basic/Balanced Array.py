Link : https://practice.geeksforgeeks.org/problems/balanced-array07200720/1?page=3&difficulty[]=-1&status[]=unsolved&sortBy=submissions

Code :

# User function Template for python3

class Solution:
    def minValueToBalance(self,a,n):
        mid = len(a) // 2
        left_half = a[:mid]
        right_half = a[mid:]
        return abs(sum(left_half) - sum(right_half))


# Driver Code Starts
# Initial Template for Python 3

t=int(input())
for _ in range(0,t):
    n=int(input())
    a = list(map(int,input().split()))
    ob = Solution()
    ans=ob.minValueToBalance(a,n)
    print(ans)

# Driver Code Ends
