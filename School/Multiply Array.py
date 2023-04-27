Link : https://practice.geeksforgeeks.org/problems/multiply-array-1658312632/1?page=1&difficulty[]=-2&status[]=unsolved&sortBy=submissions

Code :

# Initial Template for Python 3

class Solution:
    def longest(self, arr, n):
        product = 1
        for i in arr:
            product *= i
        return product


# Driver Code Starts
    
def main():
    T = int(input())
    while(T > 0):
        n = int(input())
        arr = [int(x) for x in input().strip().split()]
        ob = Solution()
        print(ob.longest(arr, n))
        T -= 1

if __name__ == "__main__":
    main()

# Driver Code Ends
