Link : https://practice.geeksforgeeks.org/problems/union-of-two-sorted-arrays-1587115621/1?page=4&difficulty[]=-1&difficulty[]=0&status[]=unsolved&sortBy=submissions

Code :

# User function Template for python3

class Solution:
    
    #Function to return a list containing the union of the two arrays.
    def mergeArrays(self,a,b,n,m):
        set1 = set(a)
        set2 = set(b)
        return sorted(list(set1.union(set2)))        


# Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        n,m = map(int,input().strip().split())
        a = list(map(int,input().strip().split()))
        b = list(map(int,input().strip().split()))
        ob=Solution()
        li = ob.mergeArrays(a,b,n,m)
        for val in li:
            print(val, end = ' ')
        print()
# Driver Code Ends
