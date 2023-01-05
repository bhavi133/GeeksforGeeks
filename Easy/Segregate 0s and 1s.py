Link : https://practice.geeksforgeeks.org/problems/segregate-0s-and-1s5106/1?page=1&status[]=bookmarked&sortBy=submissions

Code :

#User function Template for python3

class Solution:
    def segregate0and1(self, arr, n):
        return arr.sort()


# Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ob.segregate0and1(arr, n)
        print(*arr)
        tc -= 1

# Driver Code Ends
