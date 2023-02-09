Link : https://practice.geeksforgeeks.org/problems/upper-case-conversion5419/1?page=1&difficulty[]=-2&status[]=unsolved&sortBy=submissions

Code :

# User function Template for python3

class Solution:
    def transform(self, s):
        return s.title()


# Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        s = input().strip()
        ob = Solution()
        print(ob.transform(s))
# Driver Code Ends
