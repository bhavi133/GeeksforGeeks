Link : https://practice.geeksforgeeks.org/problems/find-the-odd-occurence4820/1?page=1&status[]=bookmarked&sortBy=submissions

Code :

# User function Template for python3

class Solution:
    def getOddOccurrence(self, arr, n):
        dic = {} 
        for i in arr:
            if i in dic:
                dic[i] += 1
            else:
                dic[i] = 1
                
        for i, j in dic.items():
            if j % 2 == 1:
                return i


# Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.getOddOccurrence(arr, n)
        print(ans)
        tc -= 1

# Driver Code Ends
