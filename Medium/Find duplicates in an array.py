Link : https://practice.geeksforgeeks.org/problems/find-duplicates-in-an-array/1?page=1&difficulty[]=0&difficulty[]=1&sortBy=submissions

Code :

from collections import Counter

class Solution:
    def duplicates(self, arr, n): 
        l1 = []
        l2 = [-1]
        dic = Counter(arr)
        for key, val in dic.items():
            if val > 1:
                l1.append(key)
            else:
                pass
        
        l1.sort()
        if len(l1) == 0:
            return l2
        else:
            return l1

# Driver Code Starts
if(__name__=='__main__'):
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        res = Solution().duplicates(arr, n)
        for i in res:
            print(i,end=" ")
        print()
# Driver Code Ends
