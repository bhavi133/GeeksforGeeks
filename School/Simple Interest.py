Link : https://practice.geeksforgeeks.org/problems/simple-interest3457/0

Code :

# User function Template for python3

class Solution:
    def simpleInterest(self,A,B,C):
        return (A * B * C) / 100
 

# Driver Code Starts
# Initial Template for Python 3

if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        P,R,T=map(int,input().strip().split(' '))
        ob=Solution()
        print('%.2f'%ob.simpleInterest(P,R,T))

# Driver Code Ends
