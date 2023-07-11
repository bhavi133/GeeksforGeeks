Link : https://practice.geeksforgeeks.org/problems/counting-elements-in-two-arrays/1?page=1&status[]=unsolved&category[]=Arrays&sortBy=submissions

Code :

# User function Template for python3

from bisect import bisect_right

class Solution:
    def countEleLessThanOrEqual(self,arr1,n1,arr2,n2):
        arr2.sort()
        l = []
        for i in arr1:
            x = bisect_right(arr2, i)
            l.append(x)
        return l


# Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    t=int(input())    
    for tcs in range(t):
        n1,n2=[int(x) for x in input().split()]
        arr1=[int(x) for x in input().split()]
        arr2=[int(x) for x in input().split()]
        res = Solution().countEleLessThanOrEqual(arr1,n1,arr2,n2)
        for i in range (len (res)):
            print (res[i], end = " ")
        print()

# Driver Code Ends
