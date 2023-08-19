Link : https://practice.geeksforgeeks.org/problems/product-is-even-or-odd3020/1?page=1&difficulty[]=-1&sprint=b177b14354b699a74784fb34752c6a69&sortBy=submissions

Code :

# User function Template for python3

class Solution:
    def EvenOdd(self, n1, n2):
        if (int(n1) * int(n2) % 2) == 0:
            return 1
        return 0


# Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        a = int(input().strip())
        b = int(input().strip())
        ob = Solution()
        ans = ob.EvenOdd(a,b)
        print(ans)

# Driver Code Ends
