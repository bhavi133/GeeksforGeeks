Link : https://practice.geeksforgeeks.org/problems/third-largest-element/1?page=2&difficulty[]=-1&status[]=unsolved&sortBy=submissions

Code :

class Solution:
    def thirdLargest(self,a, n):
        l = sorted(a, reverse=True)
        return l[2]


# Driver Code Starts
# Your code goes here
if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        print(Solution().thirdLargest(arr, n))
# Driver Code Ends
