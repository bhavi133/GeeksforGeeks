Link : https://practice.geeksforgeeks.org/problems/find-missing-and-repeating2512/1?page=1&status[]=bookmarked&sortBy=submissions

Code :

# User function Template for python3

from collections import Counter

class Solution:
    def findTwoElement(self,arr, n): 
        l1 = []
        l2 = [sum(range(1, n+1)) - sum(set(arr))]
        dic = Counter(arr)
        for i, j in dic.items():
            if (j > 1):
                l1.append(i)
        return l1 + l2
 
 
# Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__': 

    tc=int(input())
    while tc > 0:
        n=int(input())
        arr=list(map(int, input().strip().split()))
        ob = Solution()
        ans=ob.findTwoElement(arr, n)
        print(str(ans[0])+" "+str(ans[1]))
        tc=tc-1
        
# Driver Code Ends
