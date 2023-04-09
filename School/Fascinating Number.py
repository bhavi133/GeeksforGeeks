Link : https://practice.geeksforgeeks.org/problems/fascinating-number3751/1?page=1&difficulty[]=-2&status[]=unsolved&sortBy=submissions

Code :

# User function Template for python3

class Solution:
	def fascinating(self,n):
        return list('123456789') == sorted(str(n) + str(n * 2) + str(n * 3))


# Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input().strip())
        ob = Solution()
        ans = ob.fascinating(n)
        if ans:
            print("Fascinating")
        else:
            print("Not Fascinating")
        tc -= 1

# Driver Code Ends
