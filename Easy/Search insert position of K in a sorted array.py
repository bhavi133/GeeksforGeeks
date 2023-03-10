Link : https://practice.geeksforgeeks.org/problems/search-insert-position-of-k-in-a-sorted-array/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=search-insert-position-of-k-in-a-sorted-array

Code :

# User function Template for python3

class Solution:
    def searchInsertK(self, Arr, N, k):
        for i in Arr:
            if i == k:
                return Arr.index(i)
            else:
                Arr.append(k)
                return sorted(Arr).index(k)
        
 
# Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range (t):
        N = int(input())
        Arr = input().split()
        for itr in range(N):
            Arr[itr] = int(Arr[itr])
        k = int(input())
        ob = Solution()
        print(ob.searchInsertK(Arr, N, k))

# Driver Code Ends
