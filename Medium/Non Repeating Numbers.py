Link : https://practice.geeksforgeeks.org/problems/finding-the-numbers0215/1?page=4&difficulty[]=1&status[]=unsolved&sortBy=submissions

Code :

# User function Template for python3

import collections

class Solution:
	def singleNumber(self, nums):
	    l = []
        dic = collections.Counter(nums)
        for i, j in dic.items():
            if j == 1:
                l.append(i)
        return sorted(l)

# Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		v = list(map(int,input().split()))
		ob = Solution();
		ans = ob.singleNumber(v)
		for i in ans:
			print(i, end = " ")
		print()

# Driver Code Ends
