Link : https://practice.geeksforgeeks.org/problems/binary-number-to-decimal-number3525/1?page=2&difficulty[]=-1&status[]=unsolved&sortBy=submissions

Code :

# User function Template for python3

class Solution:
	def binary_to_decimal(self, str):
		return int(str, 2)


# Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		str = input()
		ob = Solution();
		ans = ob.binary_to_decimal(str)
		print(ans)

# Driver Code Ends
