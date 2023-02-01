Link : https://practice.geeksforgeeks.org/problems/print-elements-of-array4910/1?page=1&difficulty[]=-2&sortBy=submissions

Code :

# User function Template for python3
class Solution:
	def printArray(self,arr, n):
	    for i in arr:
	        print(i, end=" ")


# Driver Code Starts
# Initial Template for Python 3

# Driver code 
if __name__ == "__main__": 		
    tc=int(input())
    while tc > 0:
        n=int(input().strip())
        arr=list(map(int, input().strip().split()))
        ob = Solution()
        ob.printArray(arr, n)
        print()
        tc=tc-1
# Driver Code Ends
