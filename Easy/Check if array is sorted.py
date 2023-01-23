Link : https://practice.geeksforgeeks.org/problems/check-if-an-array-is-sorted0701/1?page=5&difficulty[]=-1&difficulty[]=0&status[]=unsolved&sortBy=submissions

Code :

# User function Template for python3

class Solution:
    def arraySortedOrNot(self, arr, n):
        return arr == sorted(arr)


# Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        
        ob = Solution()
        ans = ob.arraySortedOrNot(arr, n)
        if ans:
            print(1)
        else:
            print(0)
        tc -= 1

# Driver Code Ends
