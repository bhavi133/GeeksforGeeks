Link : https://practice.geeksforgeeks.org/problems/missing-number-in-shuffled-array0938/1?page=3&difficulty[]=-1&status[]=unsolved&sortBy=submissions

Code :

# User function Template for python3

import collections

class Solution:
    def repeatingEven(self, arr, n):
        dic = collections.Counter(arr)
        l = []
        for i, j in dic.items():
            if j % 2 == 0:
                l.append(i)
        if len(sorted(l)) != 0:
            return sorted(l)
        return [-1]


# Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.repeatingEven(arr, n)
        for xx in ans:
            print(xx, end=" ")
        print()
        tc -= 1

# Driver Code Ends
