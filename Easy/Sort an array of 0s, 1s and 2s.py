Link : https://practice.geeksforgeeks.org/problems/sort-an-array-of-0s-1s-and-2s4231/1?page=1&difficulty[]=0&status[]=solved&sortBy=submissions

Code : 

#User function Template for python3

class Solution:
    def sort012(self,arr,n):
        return arr.sort()



# Driver Code Starts
# Initial Template for Python 3
if __name__ == '__main__':
    t=int(input())
    for _ in range(t):
        n=int(input())
        arr=[int(x) for x in input().strip().split()]
        ob=Solution()
        ob.sort012(arr,n)
        for i in arr:
            print(i, end=' ')
        print()
# Driver Code Ends
