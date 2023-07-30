Link : https://practice.geeksforgeeks.org/problems/numbers-containing-0s-from-1-to-n4704/1?page=4&sprint=b177b14354b699a74784fb34752c6a69&sortBy=latest

Code :

# User function Template for python3

class Solution:
	def CountNo(self, N):
 		# return len([i for i in range(1, N+1) if '0' in str(i)])
        
    count = 0
    for i in range(1, N+1):
        if '0' in str(i):
            count += 1
    return count


# Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		ob = Solution()
		ans = ob.CountNo(n)
		print(ans)

# Driver Code Ends
