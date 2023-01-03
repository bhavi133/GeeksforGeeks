Link : https://practice.geeksforgeeks.org/problems/odd-or-even3618/1?page=1&difficulty[]=-2&status[]=unsolved&sortBy=submissions

Code :

# User function Template for python3
class Solution:
    def oddEven (ob,N):
        # code here 
        if N % 2 == 0:
            return 'even'
        else:
            return 'odd'


# Driver Code Starts
# Initial Template for Python 3
if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        
        N=int(input())

        ob = Solution()
        print(ob.oddEven(N))
# Driver Code Ends
