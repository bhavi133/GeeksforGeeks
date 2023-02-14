Link : https://practice.geeksforgeeks.org/problems/merge-two-sorted-arrays-1587115620/1?page=2&status[]=unsolved&curated[]=1&sortBy=submissions

Code :

# User function Template for python3

class Solution:
    def merge(self,arr1,arr2,n,m):
        x = sorted(arr1 + arr2)
        arr1[::] = x[:n]
        arr2[::] = x[n:]
        return arr1 + arr2
        

# Driver Code Starts
# Initial template for Python

if __name__ == '__main__':
    t = int(input())
    for tt in range(t):
        n,m = map(int, input().strip().split())
        arr1 = list(map(int, input().strip().split()))
        arr2 = list(map(int, input().strip().split()))
        ob=Solution()
        ob.merge(arr1, arr2, n, m)
        print(*arr1,end=" ")
        print(*arr2)
# Driver Code Ends
