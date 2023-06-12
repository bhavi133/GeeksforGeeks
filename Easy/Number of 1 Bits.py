Link : https://practice.geeksforgeeks.org/problems/set-bits0143/1?page=4&difficulty[]=0&status[]=unsolved&sortBy=submissions

Code :

# User function Template for python3

class Solution:
	def setBits(self, N):
        return bin(N)[2:].count('1')


# Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		N = int(input())
		ob = Solution()
		ans = ob.setBits(N)
		print(ans)

# Driver Code Ends
