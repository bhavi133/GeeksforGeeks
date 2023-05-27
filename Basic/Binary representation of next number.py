Link : https://practice.geeksforgeeks.org/problems/binary-representation-of-next-number3648/1?page=1&difficulty[]=-2&status[]=unsolved&sortBy=submissions

Code :

class Solution:
	def binaryNextNumber(self, S):
	    # x = int(S, 2)
      # y = bin(x+1)[2:]
      # return y
        
      return bin(int(S, 2)+1)[2:]


# Driver Code Starts

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		S = input()
		ob = Solution();
		ans = ob.binaryNextNumber(S)
		print(ans)

# Driver Code Ends
