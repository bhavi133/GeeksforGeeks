Link : https://practice.geeksforgeeks.org/problems/red-or-green5711/1?page=4&difficulty[]=-1&status[]=unsolved&sortBy=submissions

Code :

# User function Template for python3

class Solution:
    def RedOrGreen(self,N,S):
        # green_count = S.count('G')
        # red_count = S.count('R')
        # if green_count > red_count:
        #     return red_count
        # else:
        #     return green_count

        return min(S.count('G'), S.count('R'))


# Driver Code Starts
# Initial Template for Python 3

if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        N=int(input())
        S=input()     
        ob=Solution()
        print(ob.RedOrGreen(N,S))

# Driver Code Ends
