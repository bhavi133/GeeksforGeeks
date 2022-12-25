Link : https://practice.geeksforgeeks.org/problems/permutations-of-a-given-string2041/1?page=1&difficulty[]=1&status[]=solved&sortBy=submissions

Code :

#User function Template for python3

from itertools import permutations

# str = 'ABC'
class Solution:
    def find_permutation(self, S):
        l = []
        x = [''.join(i) for i in permutations(S)]
        return sorted(list(set(x)))



# Driver Code Starts
# Initial Template for Python 3
if __name__ == '__main__':
	t=int(input())
	for i in range(t):
		S=input()
		ob = Solution()
		ans = ob.find_permutation(S)
		for i in ans:
			print(i,end=" ")
		print()
# Driver Code Ends
