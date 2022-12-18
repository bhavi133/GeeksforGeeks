Link : https://practice.geeksforgeeks.org/problems/value-equal-to-index-value1330/1?page=1&difficulty[]=-2&status[]=solved&sortBy=submissions

Code : 

#User function Template for python3

class Solution:

	def valueEqualToIndex(self,arr, n):
	    l = []
        for i, j in enumerate(arr, start=1):
            if i == j:
                l.append(i)
        return l
	    
	        
# Driver Code Starts
if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.valueEqualToIndex(arr, n)
        if len(ans) == 0:
            print("Not Found")
        else:
            for x in ans:
                print(x, end=" ")
            print()
        tc -= 1
# Driver Code Ends
