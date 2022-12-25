Link : https://practice.geeksforgeeks.org/problems/anagram-1587115620/1?page=1&difficulty[]=0&status[]=solved&sortBy=submissions

Code : 

#User function Template for python3

class Solution:
    
    #Function is to check whether two strings are anagram of each other or not.
    def isAnagram(self,a,b):
        x = list(a)
        y = list(b)
        sort1 = sorted(x)
        sort2 = sorted(y)
        return sort1 == sort2


# Driver Code Starts
# Initial Template for Python 3
if __name__=='__main__':
    t = int(input())
    for i in range(t):
        a,b=map(str,input().strip().split())
        if(Solution().isAnagram(a,b)):
            print("YES")
        else:
            print("NO") 
# Driver Code Ends
