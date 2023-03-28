Link : https://practice.geeksforgeeks.org/problems/java-delete-alternate-characters4036/1?page=1&difficulty[]=-2&status[]=unsolved&sortBy=submissions

Code :

# User function Template for python3
class Solution:
    def delAlternate (ob, S):
        return S[::2]


# Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        S = input()      
        ob = Solution()
        print(ob.delAlternate(S))

# Driver Code Ends
