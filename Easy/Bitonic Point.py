Link : https://practice.geeksforgeeks.org/problems/maximum-value-in-a-bitonic-array3001/1?page=1&status[]=unsolved&curated[]=8&sortBy=submissions

Code :

# User function Template for python3

class Solution:
	def findMaximum(self,arr, n):
		return sorted(arr)[-1]


# Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.findMaximum(arr, n)
        print(ans)
        tc -= 1

# Driver Code Ends
