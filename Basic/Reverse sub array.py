Link : https://practice.geeksforgeeks.org/problems/reverse-sub-array5620/1?page=3&difficulty[]=-1&status[]=unsolved&sortBy=submissions

Code :

# User function Template for python3

class Solution:
	def reverseSubArray(self,arr, n, l, r):
		arr[l-1:r] = arr[l-1:r][::-1]
		return arr


# Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        l, r = list(map(int, input().strip().split()))
        ob = Solution()
        ob.reverseSubArray(arr, n, l, r)
        for x in arr:
            print(x, end=" ")
        print()
        tc -= 1

# Driver Code Ends
