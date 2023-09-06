Link : https://practice.geeksforgeeks.org/problems/sum-of-distinct-elements4801/1

Code :

# User function Template for python3

class Solution:	
	def findSum(self,arr, n):
		sum = 0
		for i in set(arr):
		    sum += i
		return sum


# Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.findSum(arr, n)
        print(ans)
        tc -= 1

# Driver Code Ends
