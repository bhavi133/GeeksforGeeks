Link : https://practice.geeksforgeeks.org/problems/find-first-and-last-occurrence-of-x0849/1?page=1&difficulty[]=0&sprint=b177b14354b699a74784fb34752c6a69&sortBy=submissions

Code :

# User function Template for python3

class Solution:
    def indexes(self, v, x):
        l = []
        for i in range(len(v)):
            if v[i] == x:
                l.append(i)
        if len(l) == 0:
            return [-1, -1]
        elif len(l) == 1:
            return [l[0], l[0]]
        else:
            return [l[0], l[-1]]


# Driver Code Starts
# Initial Template for Python 3

def main():
    T = int(input())
    while(T > 0):
        n = int(input())
        a = [int(x) for x in input().strip().split()]
        k = int(input())
        obj = Solution()
        ans = obj.indexes(a, k)
        if ans[0]==-1 and ans[1]==-1:
            print(-1)
        else:
            print(ans[0], end=' ')
            print(ans[1])
        T -= 1

if __name__ == "__main__":
    main()

# Driver Code Ends
