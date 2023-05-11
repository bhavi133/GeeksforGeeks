Link : https://practice.geeksforgeeks.org/problems/sum-of-ap-series4512/1?page=1&difficulty[]=-2&status[]=unsolved&sortBy=submissions

Code :

# User function Template for python3

class Solution:
	def sum_of_ap(self, n, a, d):
		l = []
		for i in range(n):
		    l.append(a + i * d)
		return sum(l)
		
 		# return sum([(a + i * d) for i in range(n)])


# Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n, a, d = input().split()
		n = int(n)
		a = int(a)
		d = int(d)
		ob = Solution();
		ans = ob.sum_of_ap(n, a, d)
		print(ans)

# Driver Code Ends
