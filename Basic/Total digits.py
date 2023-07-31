Link : https://practice.geeksforgeeks.org/problems/total-digits4030/1?page=4&sprint=b177b14354b699a74784fb34752c6a69&sortBy=latest

Code :

# User function Template for python3

class Solution:
    def totalDigits (ob, n):
        # code here 
        # l = [str(i) for i in range(1, n+1)]
        # s = ""
        # for i in l:
        #     s += i
        # return len(s)
        
        s = ""
        for i in range(1, n+1):
            s += str(i)
        return len(s)


# Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        n = int(input())    
        ob = Solution()
        print(ob.totalDigits(n))

# Driver Code Ends
