Link : https://practice.geeksforgeeks.org/problems/count-odd-even/1?page=5&difficulty[]=0&status[]=unsolved&sortBy=submissions

Code :

# User function Template for python3

class Solution:
	def countOddEven(self, arr, n):
		#Code here
		even_count = 0
		odd_count = 0
		for i in arr:
		    if i % 2 == 0:
		        even_count += 1
		    else:
		        odd_count += 1
        print(odd_count, even_count)
		      

# Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    T=int(input())
    for i in range(T):
        n = int(input())
        arr = list(map(int, input().strip().split()))
    	obj = Solution()
    	obj.countOddEven(arr, n);
# Driver Code Ends
