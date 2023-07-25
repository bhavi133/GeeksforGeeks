Link : https://practice.geeksforgeeks.org/problems/maximum-repeating-number4858/1?page=1&sprint=b177b14354b699a74784fb34752c6a69&sortBy=submissions

Code :

# User function Template for python3
 
class Solution:
	def maxRepeating(self,arr, n, k):
		dic = {}
		for i in arr:
		    if i in dic:
		        dic[i] += 1
		    else:
		        dic[i] = 1
		 
		l = sorted(dic.items(), key=lambda x : x[1], reverse=True)
		return l[0][0]

 
# Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n, k = list(map(int, input().strip().split()))
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.maxRepeating(arr, n, k)
        print(ans)
        tc -= 1

# Driver Code Ends
