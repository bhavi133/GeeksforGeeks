Link : https://practice.geeksforgeeks.org/problems/binary-representation5003/1?page=1&difficulty[]=-2&status[]=unsolved&sortBy=submissions

Code :

class Solution:
	def getBinaryRep(self, n):
		  binary_string = bin(n)[2:]
      x = 30 - len(binary_string)
      y = x * '0'
      return y + binary_string
            
            
# Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		ob = Solution();
		ans = ob.getBinaryRep(n)
		print(ans)

# Driver Code Ends
