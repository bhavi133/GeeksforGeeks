Link : https://practice.geeksforgeeks.org/problems/ones-complement5928/1?page=3&difficulty[]=-1&status[]=unsolved&sortBy=submissions

Code :

# User function Template for python3

class Solution:
    def onesComplement(self,N):
        # s = ""
        # for i in bin(N)[2:]:
        #     if i == '1':
        #         s += '0'
        #     else:
        #         s += '1'
        # return int(s, 2) 
        
        s = bin(N)[2:]
        s = s.replace('0', '*')
        s = s.replace('1', '0')
        s = s.replace('*', '1')
        return int(s, 2)        
    

# Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N = int(input())
        ob = Solution()
        print(ob.onesComplement(N))

# Driver Code Ends
