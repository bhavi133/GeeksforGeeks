Link : https://practice.geeksforgeeks.org/problems/vowel-or-not0831/1?page=1&difficulty[]=-2&status[]=unsolved&sortBy=submissions

Code :

# User function Template for python3
class Solution:
    def isVowel (ob,c):
        if (c == 'a' or c == 'e' or c == 'i' or c == 'o' or c == 'u' or c == 'A' or c == 'E' or c == 'I' or c == 'O' or c == 'U'):
            return "YES"
        else:
            return "NO"


# Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):        
        c=input()
        ob = Solution()
        print(ob.isVowel(c))

# Driver Code Ends
