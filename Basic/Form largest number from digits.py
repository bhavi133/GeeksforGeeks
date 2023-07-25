Link : https://practice.geeksforgeeks.org/problems/form-largest-number-from-digits5430/1?page=1&sprint=b177b14354b699a74784fb34752c6a69&sortBy=submissions

Code :

# User function Template for python3

class Solution:
    def MaxNumber(self, arr, n):
        arr = sorted(arr, reverse=True)
        return "".join(list(map(str, arr)))
        

# Driver Code Starts
# Initial Template for Python 3

def main():
    T = int(input())
    while(T > 0):
        n = int(input())
        a = [int(x) for x in input().strip().split()]
        ob = Solution()
        print(ob.MaxNumber(a, n))
        T -= 1

if __name__ == "__main__":
    main()
  
# Driver Code Ends
