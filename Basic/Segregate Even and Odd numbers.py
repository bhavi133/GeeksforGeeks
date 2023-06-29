Link : https://practice.geeksforgeeks.org/problems/segregate-even-and-odd-numbers4629/1?page=3&difficulty[]=-1&status[]=unsolved&sortBy=submissions

Code :

# User function Template for python3

class Solution:
	def segregateEvenOdd(self,arr, n):
	    even = []
        odd = []
        for i in arr:
            if i % 2 == 0:
                even.append(i)
            else:
                odd.append(i)
        arr[:] = sorted(even) + sorted(odd)
        return arr


# Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ob.segregateEvenOdd(arr, n)
        for x in arr:
            print(x, end=" ")
        print()
        tc -= 1

# Driver Code Ends
