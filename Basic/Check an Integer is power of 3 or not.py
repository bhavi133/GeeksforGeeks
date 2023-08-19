Link : https://practice.geeksforgeeks.org/problems/check-a-integer-is-power-of-3-or-not3850/1?page=2&difficulty[]=-1&sprint=b177b14354b699a74784fb34752c6a69&sortBy=submissions

Code :

# User function Template for python3

class Solution:
    def isPowerof3 (ob,N):
        if N == 1:
            return 'Yes'
        else:
            for i in range(1, 31):
                if 3 ** i == N:
                    return 'Yes'
            return 'No'

 
# Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):  
        N = int(input())
        ob = Solution()
        print(ob.isPowerof3(N))
# Driver Code Ends
