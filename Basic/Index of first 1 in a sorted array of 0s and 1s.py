Link : https://practice.geeksforgeeks.org/problems/index-of-first-1-in-a-sorted-array-of-0s-and-1s4048/1?page=3&difficulty[]=-1&status[]=unsolved&sortBy=submissions

Code :

# User function Template for python3

class Solution:
    def firstIndex(self, arr, n):
        for i in arr:
            if i == 1:
                return arr.index(i)
        else:
            return -1
        
        
# Driver Code Starts
# Initial Template for Python 3

def main():
    T = int(input())
    while(T > 0):
        n = int(input())
        a = [int(x) for x in input().strip().split()]
        ob = Solution()
        print(ob.firstIndex(a, n))
        T -= 1

if __name__ == "__main__":
    main()

# Driver Code Ends
