Link : https://practice.geeksforgeeks.org/problems/second-largest3735/1?page=1&difficulty[]=-2&status[]=solved&sortBy=submissions
  
Code :
  
#User function Template for python3
class Solution:

	def print2largest(self,arr, n):
	    y = list(set(arr))
	    if len(y) <= 1:
	        return -1
	    else:
	        x = sorted(y, reverse=True)
		    return x[1]


# Driver Code Starts
if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.print2largest(arr, n)
        print(ans)
        tc -= 1
# Driver Code Ends
