Link : https://practice.geeksforgeeks.org/problems/print-first-letter-of-every-word-in-the-string3632/0

Code :

# User function Template for python3

class Solution:
	def firstAlphabet(self, S):
		return "".join([i[0] for i in S.split()])
		
    # 	s = S.split()
    # 	l = []
    # 	for i in s:
    # 		l.append(i[0])
    # 	return "".join(l)


# Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		S = input()
		ob = Solution()
		answer = ob.firstAlphabet(S)
		print(answer)

# Driver Code Ends
