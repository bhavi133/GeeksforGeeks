Link : https://practice.geeksforgeeks.org/problems/find-the-median0527/1?page=1&difficulty[]=-2&sortBy=submissions

Code :
  
#User function Template for python3
class Solution:
	def find_median(self, v):
	    l = sorted(v, reverse=True)
        left1 = 0
        right1 = len(l) - 1
        left2 = 0
        right2 = len(l)
        median1 = (left1 + right1) // 2
        median2 = (left2 + right2) // 2
        if len(l) % 2 != 0:
            return l[median1]
        else:
            return ((l[median1] + l[median2])//2)


# Driver Code Starts
# Initial Template for Python 3
if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		v = list(map(int,input().split())) 
		ob = Solution();
		ans = ob.find_median(v)
		print(ans)
# Driver Code Ends
