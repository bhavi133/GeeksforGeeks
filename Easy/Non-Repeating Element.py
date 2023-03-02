Link : https://practice.geeksforgeeks.org/problems/non-repeating-element3958/1?page=1&status[]=unsolved&curated[]=2&sortBy=submissions

Code :

# User function Template for python3

class Solution:
    def firstNonRepeating(self, arr, n):
        dic = {}
        for i in arr:
            if i in dic:
                dic[i] += 1
            else:
                dic[i] = 1
                
        for i in arr:
            if dic[i] == 1:
                return i
                break
        else:
            return 0
                
 
# Driver Code Starts
# Initial Template for Python 3

from collections import defaultdict 

for _ in range(0,int(input())):
    n = int(input())
    arr = list(map(int,input().strip().split()))
    ob = Solution()
    print(ob.firstNonRepeating(arr, n))
    
# Driver Code Ends
