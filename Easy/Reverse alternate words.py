Link : https://practice.geeksforgeeks.org/problems/c-alternate-words-in-reverse-order0653/1?page=4&difficulty[]=-1&difficulty[]=0&status[]=unsolved&sortBy=submissions

Code :

# User function Template for python3

class Solution:
    def reverseAlternate(self, Str):
        s = Str.split()
        l = []
        for i in range(len(s)):
            if i % 2 == 1:
                s[i] = s[i][::-1]
        return " ".join(s)
        
# Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        Str = input()
        solObj = Solution()
        print(solObj.reverseAlternate(Str))

# Driver Code Ends
