Link : https://practice.geeksforgeeks.org/problems/sum-of-array2326/1?page=1&difficulty[]=-2&status[]=solved&sortBy=submissions

Code :

# User function Template for python3

class Solution:
	def _sum(self,arr, n):
   		sum = 0
   		for i in arr:
   		    sum += i
   	    return sum
   		

# Driver Code Starts
# Initial Template for Python 3

if __name__ == "__main__": 		
    tc=int(input())
    while tc > 0:
        n=int(input())
        arr=list(map(int , input().strip().split()))
        ob = Solution()
        ans = ob._sum(arr, n)
        print(ans)
        tc=tc-1

# Driver Code Ends
