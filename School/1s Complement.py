Link : https://practice.geeksforgeeks.org/problems/1s-complement2819/1?page=3&difficulty[]=-1&status[]=unsolved&sortBy=submissions

Code :

# User function Template for python3

class Solution:
    def onesComplement(self,S,N):
        result = ""
        for i in str(S):
            if i == '1':
                result += '0'
            else:
                result += '1'
        return result
        

# Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N = int(input())
        S = input()
        ob = Solution()
        print(ob.onesComplement(S,N))

# Driver Code Ends
