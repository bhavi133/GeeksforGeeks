Link : https://practice.geeksforgeeks.org/problems/amicable-pair0804/1?page=2&difficulty[]=0&sprint=b177b14354b699a74784fb34752c6a69&sortBy=submissions

Code :

# User function Template for python3

class Solution:
    def isAmicable(self, A , B):
        sum = 0
        for i in range(1, A):
            if A % i == 0:
                sum += i
        if sum == B:
            return 1
        else:
            return 0


# Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        A,B=map(int,input().split()) 
        ob = Solution()
        print(ob.isAmicable(A,B))

# Driver Code Ends
