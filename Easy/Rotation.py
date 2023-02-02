Link : https://practice.geeksforgeeks.org/problems/rotation4723/1?page=6&difficulty[]=0&difficulty[]=1&status[]=unsolved&sortBy=submissions

Code :

# User function Template for python3
class Solution:
    def findKRotation(self,arr,  n):
        return arr.index(sorted(arr)[0]) - arr.index(arr[0]) 


# Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':

	tc=int(input())
	while tc > 0:
		n=int(input())
		a=list(map(int , input().strip().split()))
		ob = Solution()
		ans=ob.findKRotation(a, n)
		print(ans)
		tc=tc-1
    
# Driver Code Ends
