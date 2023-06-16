Link : https://practice.geeksforgeeks.org/problems/fighting-the-darkness3949/1?page=3&difficulty[]=-1&status[]=unsolved&sortBy=submissions

Code :

class Solution:
    def maxDays(self, arr, n):
        return max(arr)

 
# Driver Code Starts

if __name__ == '__main__': 
    t=int(input())
    for _ in range(0,t):
        n=int(input())
        arr = list(map(int,input().split()))
        ob = Solution()
        print(ob.maxDays(arr,n))

# Driver Code Ends
