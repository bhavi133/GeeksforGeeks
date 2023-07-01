Link : https://practice.geeksforgeeks.org/problems/element-appearing-once2552/1?page=2&difficulty[]=1&status[]=unsolved&sortBy=submissions

Code :

# User function Template for python3

class Solution:
    def search(self, A, N):
        dic = {}
        for i in A:
            if i in dic:
                dic[i] += 1
            else:
                dic[i] = 1
        
        for i, j in dic.items():
            if j == 1:
                return i


# Driver Code Starts
# Initial Template for Python 3

if __name__ == "__main__":
	t = int (input ())
	for tc in range (t):
		n = int (input ())
		arr = list(map(int, input().split()))
		ob = Solution()
		print(ob.search(arr, n)) 

# Driver Code Ends
