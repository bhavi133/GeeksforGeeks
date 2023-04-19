Link : https://practice.geeksforgeeks.org/problems/lower-case-to-upper-case3410/1?page=1&difficulty[]=-2&status[]=unsolved&sortBy=submissions

Code :

# User function Template for python3

class Solution:
    def to_upper(self, str):
        return str.upper()


# Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        str = input().strip()
        ob = Solution()
        print(ob.to_upper(str))

# Driver Code Ends
