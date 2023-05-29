Link : https://practice.geeksforgeeks.org/problems/c-program-to-remove-consonants-from-a-string1945/1?page=5&difficulty[]=-1&status[]=unsolved&status[]=bookmarked&sortBy=submissions

Code :

# User function Template for python3

class Solution:
    def removeConsonants(self, s):
        vowels = "aeiouAEIOU"
        result = ""
        for i in s:
            if i in vowels:
                result += i
        if len(result) != 0:
            return result
        return "No Vowel"


# Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        s = input()
        ob = Solution()
        print(ob.removeConsonants(s))

# Driver Code Ends
