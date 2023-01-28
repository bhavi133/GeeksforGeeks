Link : https://practice.geeksforgeeks.org/problems/merge-k-sorted-arrays/1?page=7&difficulty[]=1&status[]=unsolved&sortBy=submissions

Code :

# User function Template for python3

class Solution:
    def mergeKArrays(self, arr, K):
        l = []
        for i in arr:
            for j in i:
                l.append(j)
        return sorted(l)


# Driver Code Starts
# Initial Template for Python 3

if __name__=="__main__":
    t=int(input())
    for _ in range(t):
        n=int(input())
        numbers=[[ 0 for _ in range(n) ] for _ in range(n) ]
        line=input().strip().split()
        for i in range(n):
            for j in range(n):
                numbers[i][j]=int(line[i*n+j])
        ob = Solution();
        merged_list=ob.mergeKArrays(numbers, n)
        for i in merged_list:
            print(i,end=' ')
        print()
# Driver Code Ends
