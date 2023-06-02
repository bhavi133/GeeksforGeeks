Link : https://practice.geeksforgeeks.org/problems/remove-characters-from-alphanumeric-string0648/1?page=1&difficulty[]=-2&status[]=unsolved&sortBy=submissions

Code :

# User function Template for python3

class Solution:
	def removeCharacters(self, S):
		string = ""
		for i in S:
		    if i.isnumeric():
		        string += i
		return string


# Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		s = input()		
		ob = Solution()	
		answer = ob.removeCharacters(s)		
		print(answer)

# Driver Code Ends
