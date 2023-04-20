Link : https://practice.geeksforgeeks.org/problems/move-all-zeroes-to-end-of-array0751/1?page=4&difficulty[]=-1&difficulty[]=0&status[]=unsolved&sortBy=submissions

Code :

# User function Template for python3

class Solution:
	def pushZerosToEnd(self,arr, n):
        l1 = []
        l2 = []
        for i in arr:
            if i != 0:
                l1.append(i)
            else:
                l2.append(i)
        l3 = l1 + l2
        arr[::] = l3[::]
        return arr
    	

# Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ob.pushZerosToEnd(arr, n)
        for x in arr:
            print(x, end=" ")
        print()
        tc -= 1

# Driver Code Ends
