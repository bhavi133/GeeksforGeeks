Link : https://practice.geeksforgeeks.org/problems/remove-character3815/1?page=3&difficulty[]=-1&status[]=unsolved&sortBy=submissions

Code :

# User function Template for python3

class Solution:
    def removeChars (ob, string1, string2):
        result = ""
        for i in string1:
            if i not in string2:
                result += i
        return result
        
       
# Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        string1=input()
        string2=input()        
        ob = Solution()
        print(ob.removeChars(string1,string2))

# Driver Code Ends
