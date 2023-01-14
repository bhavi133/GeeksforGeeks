Link : https://practice.geeksforgeeks.org/problems/count-the-zeros2550/1?page=1&status[]=bookmarked&sortBy=submissions

Code :

# User function Template for python3
class Solution:
    def countZeroes(self, arr, n):
        zero_count = 0
        for i in arr:
            if i == 0:
                zero_count += 1
        return zero_count


# Driver Code Starts
# Initial Template for Python 3
if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.countZeroes(arr, n)
        print(ans)
        tc -= 1
# Driver Code Ends
