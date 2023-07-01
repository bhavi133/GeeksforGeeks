Link : https://practice.geeksforgeeks.org/problems/modular-exponentiation-for-large-numbers5537/1?page=2&difficulty[]=1&status[]=unsolved&sortBy=submissions

Code :

# User function Template for python3

class Solution:
	def PowMod(self, x, n, m):
		return pow(x, n, m)


# Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		x, n , m = input().split()
		x = int(x)
		n = int(n) 
		m = int(m)
		ob = Solution();
		ans = ob.PowMod(x, n, m)
		print(ans)

# Driver Code Ends
