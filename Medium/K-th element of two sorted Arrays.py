Link : https://practice.geeksforgeeks.org/problems/k-th-element-of-two-sorted-array1317/1?page=3&difficulty[]=1&status[]=unsolved&sortBy=submissions

Code :

# User function Template for python3

class Solution:
    def kthElement(self,  arr1, arr2, n, m, k):
        l = arr1 + arr2
        return sorted(l)[k-1]
        
         
# Driver Code Starts
# Initial Template for Python 3

def main():
    T = int(input())
    while(T > 0):
        sz = [int(x) for x in input().strip().split()]
        n, m, k = sz[0], sz[1], sz[2]
        a = [int(x) for x in input().strip().split()]
        b = [int(x) for x in input().strip().split()]
        ob = Solution()
        print(ob.kthElement( a, b, n, m, k))
        T -= 1

if __name__ == "__main__":
    main()

# Driver Code Ends
