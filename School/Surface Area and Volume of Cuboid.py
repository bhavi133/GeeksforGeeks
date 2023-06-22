Link : https://practice.geeksforgeeks.org/problems/surface-area-and-volume-of-cuboid0522/1?page=2&difficulty[]=-2&status[]=unsolved&sortBy=submissions

Code :

# User function Template for python3

class Solution:
	def find(self, l, b, h):
		area = 2 * ((b * h) + (h * l) + (l * b))
		volume = l * b * h
		return area, volume


# Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		l, b, h = input().split()
		l = int(l); b = int(b); h = int(h);
		ob = Solution()
		ans = ob.find(l, b, h)
		for _ in ans:
			print(_, end = " ")
		print()

# Driver Code Ends
