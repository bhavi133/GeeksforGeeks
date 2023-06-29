Link : https://practice.geeksforgeeks.org/problems/sort-first-half-in-ascending-and-second-half-in-descending1714/1?page=3&difficulty[]=-1&status[]=unsolved&sortBy=submissions

Code :

# User function Template for python3

class Solution:
    def customSort(self, arr, n):
        x = (len(arr) // 2)
        first_half = arr[:x]
        second_half = arr[x:]
        arr[:] = sorted(first_half) + sorted(second_half, reverse=True)
        return arr


# Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input().strip())
        arr = list(map(int, input().strip().split()))
        Solution().customSort(arr, n)
        for x in arr:
            print(x, end=" ")
        print()
        tc -= 1

# Driver Code Ends
