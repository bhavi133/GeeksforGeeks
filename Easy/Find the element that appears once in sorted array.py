Link : https://practice.geeksforgeeks.org/problems/find-the-element-that-appears-once-in-sorted-array0624/1?page=6&difficulty[]=-1&difficulty[]=0&status[]=unsolved&sortBy=submissions

Code :

# User function Template for python3

class Solution:
    def findOnce(self,arr : list, n : int):
        # Complete this function
        dic = {}
        for i in arr:
            if i in dic:
                dic[i] += 1
            else:
                dic[i] = 1
        
        for i, j in dic.items():
            if j == 1:
                return i


# Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = [int(x) for x in input().strip().split()]
        ob = Solution()
        print(ob.findOnce(arr, n))
# Driver Code Ends
