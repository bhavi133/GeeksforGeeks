Link : https://practice.geeksforgeeks.org/problems/binary-representation-of-previous-number0638/1?page=3&difficulty[]=-1&status[]=unsolved&status[]=bookmarked&sortBy=submissions

Code :

# User function Template for python3
class Solution:
    def binaryPreviousNumber(self, S):
        return bin(int(S, 2)-1)[2:]


# Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    T=int(input())
	  for i in range(T):
        S = input()
		    ob = Solution()
		    ans = ob.binaryPreviousNumber(S)
		    print(ans)

# Driver Code Ends
