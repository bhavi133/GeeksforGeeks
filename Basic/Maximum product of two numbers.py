Link : https://practice.geeksforgeeks.org/problems/maximum-product-of-two-numbers2730/1?page=1&difficulty[]=-1&sprint=b177b14354b699a74784fb34752c6a69&sortBy=submissions

Code :

# User function Template for python3

class Solution:
	def maxProduct(self,arr, n):
	    arr = sorted(arr, reverse=True)
      return arr[0] * arr[1]


# Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.maxProduct(arr, n)
        print(ans)
        tc -= 1

# Driver Code Ends
