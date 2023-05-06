Link : https://practice.geeksforgeeks.org/problems/sort-in-specific-order2422/1?page=3&difficulty[]=-1&status[]=unsolved&sortBy=submissions

Code :

# User function Template for python3

class Solution:
    def sortIt(self, arr, n):
        even = []
        odd = []
        for i in arr:
            if i % 2 == 0:
                even.append(i)
            else:
                odd.append(i)
        
        arr[:] = sorted(odd, reverse=True) + sorted(even)
        return arr


# Driver Code Starts
# Initial Template for Python 3

def main():
    T = int(input())
    while(T > 0):
        n = int(input())
        a = [int(x) for x in input().strip().split()]
        ob = Solution()
        ob.sortIt(a, n)
        print(*a)
        T -= 1

if __name__ == "__main__":
    main()
  
# Driver Code Ends
